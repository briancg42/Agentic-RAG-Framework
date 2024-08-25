from fastapi import FastAPI, File, UploadFile, HTTPException, Form
from fastapi.responses import JSONResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware

import os
import logging

app = FastAPI()

# Allow all origins for simplicity; adjust according to your needs
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Consider specifying domains in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Directories to store uploads and generated files
UPLOAD_DIRECTORY = "./uploads"
GENERATED_DIRECTORY = "./generated"
os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)
#os.makedirs(GENERATED_DIRECTORY, exist_ok=True)

collections = {}

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.get("/")
async def read_root():
    return {
        "message":
        "Welcome to the FastAPI service. Use the endpoints to interact."
    }

@app.post("/upload/")
async def upload_file(collection: str = Form(...), file: UploadFile = File(...)):
    if not collection:
        raise HTTPException(status_code=422, detail="Collection name must be provided.")

    # Check allowed file extensions
    allowed_extensions = {".txt", ".pdf", ".md"}
    file_extension = os.path.splitext(file.filename)[1].lower()
    if file_extension not in allowed_extensions:
        logger.info(f"Unsupported file type: {file_extension}")
        raise HTTPException(status_code=415, detail=f"Unsupported file type: {file_extension}")

    collection_dir = os.path.join(UPLOAD_DIRECTORY, collection)
    os.makedirs(collection_dir, exist_ok=True)

    file_path = os.path.join(collection_dir, file.filename)
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    if collection not in collections:
        collections[collection] = []
    collections[collection].append(file.filename)

    logger.info(f"File {file.filename} uploaded to collection {collection}")

    return {"filename": file.filename, "collection": collection}

@app.get("/collections/")
async def get_collections():
    return JSONResponse(content=collections)


@app.get("/frameworks/")
async def get_frameworks():
    frameworks = [
        "Basic Marketing Essentials", "Advanced Strategy Framework",
        "Product Launch Template"
    ]
    return JSONResponse(content=frameworks)


@app.post("/generate/")
async def generate_document(collection: str, framework: str):
    if collection not in collections:
        raise HTTPException(status_code=404, detail="Collection not found")

    generated_results = {}
    for doc in collections[collection]:
        # Placeholder for actual generation logic
        generated_content = f"Generated content for {doc} using {framework}"
        generated_file_path = os.path.join(GENERATED_DIRECTORY,
                                           f"{doc}_generated.txt")

        with open(generated_file_path, "w") as f:
            f.write(generated_content)

        generated_results[doc] = f"/download/{doc}_generated.txt"

    return JSONResponse(content=generated_results)


@app.get("/download/{filename}")
async def download_generated_file(filename: str):
    file_path = os.path.join(GENERATED_DIRECTORY, filename)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")
    return FileResponse(file_path)
