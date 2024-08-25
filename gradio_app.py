import gradio as gr
import requests

import os
import logging

# URL of the FastAPI backend (Replace with your actual Replit URL)
API_URL = "https://9bbfca76-e08b-4c6d-9cd5-b8a283961ee9-00-1ip1oy6vo31oy.riker.replit.dev"  # Update this with your Replit URL

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def upload_file(file, collection_name):
    if not collection_name:
        return "Please provide a collection name."

    if file is None:
        return "Please upload a file."

    try:
        # Read the file and send it to the FastAPI server
        with open(file.name, "rb") as f:
            files = {"file": (os.path.basename(file.name), f)}
            response = requests.post(f"{API_URL}/upload/",
                                     files=files,
                                     data={"collection": collection_name})
            if response.status_code == 200:
                return f"Uploaded {os.path.basename(file.name)} to collection {collection_name}"
            else:
                return f"Failed to upload {os.path.basename(file.name)} with status code {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"


# Create a Gradio interface
iface = gr.Interface(
    fn=upload_file,
    inputs=[
        gr.File(label="Upload PDF, TXT, or Markdown files"),
        gr.Textbox(label="Collection Name", placeholder="default_collection")
    ],
    outputs="text",
    title="File Upload System",
    description="Upload files to the FastAPI server using Gradio.")

# Launch the interface and set `share=True` to get a public URL
iface.launch(share=True)
