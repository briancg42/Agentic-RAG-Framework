import streamlit as st
import requests
import os

# URL of the FastAPI backend (Use the Replit URL assigned to your FastAPI service)
API_URL = "https://9bbfca76-e08b-4c6d-9cd5-b8a283961ee9-00-1ip1oy6vo31oy.riker.replit.dev"

st.title("Automated Copywriting System")

# Upload section
st.header("Upload Files")
collection_name = st.text_input("Collection Name", "default_collection")
uploaded_files = st.file_uploader("Upload PDF or TXT files", accept_multiple_files=True)

if st.button("Upload Files"):
    if not collection_name:
        st.error("Please provide a collection name.")
    else:
        for uploaded_file in uploaded_files:
            files = {"file": (uploaded_file.name, uploaded_file.getvalue())}
            try:
                response = requests.post(f"{API_URL}/upload/", files=files, data={"collection": collection_name})
                if response.status_code == 200:
                    st.success(f"Uploaded {uploaded_file.name} to collection {collection_name}")
                else:
                    st.error(f"Failed to upload {uploaded_file.name} with status code {response.status_code}")
            except requests.exceptions.RequestException as e:
                st.error(f"An error occurred: {e}")