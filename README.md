# Agentic-RAG-Framework

## Overview

The **Agentic-RAG-Framework** is a platform designed to automate and enhance marketing strategies using AI-driven workflows. It leverages retrieval-augmented generation (RAG) and AI agents to streamline the creation of marketing assets and frameworks.

## Features

- **File Management System**: Efficiently handle and process various file types.
- **AI Integration**: Use AI models for generating marketing content.
- **Marketing Frameworks**: Implement frameworks like the Basic Marketing Essentials.
- **RAG Workflows**: Integrate retrieval-augmented generation techniques.
- **Langchain AI Agents**: Automate processes with AI agents.

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.8+
- Docker
- Docker Compose
- PostgreSQL (for deploying on Render or similar platforms)

### Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/briancg42/Agentic-RAG-Framework.git
   cd Agentic-RAG-Framework
   ```

2. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up the Database**:

   - **PostgreSQL with pgvector**: Use a PostgreSQL database to store structured data, such as marketing frameworks and client information. Make sure to add the `pgvector` extension for vector storage.
   - **Environment Variables**: Configure your database connection using environment variables.

4. **Run Locally**:

   - **Using Docker**:

     ```bash
     docker-compose up --build
     ```

   - **Without Docker**:

     - Start the FastAPI server:

       ```bash
       uvicorn main:app --host 0.0.0.0 --port 8000
       ```

     - Run the Gradio app:

       ```bash
       python gradio_app.py
       ```

## Project Structure

- **`app.py`**: Main application file.
- **`docker-compose.yml`**: Docker Compose configuration for orchestrating services and setting up Docker volumes.
- **`main.py`**: FastAPI application.
- **`gradio_app.py`**: Gradio interface for user interaction.
- **`uploads/`**: Directory for temporary file storage, consider using a Docker volume for persistent storage.

## Database Setup

Consider using PostgreSQL with the `pgvector` extension for storing and managing structured data:

- **Set up PostgreSQL**: Install PostgreSQL and create a database for your application.
- **Add pgvector extension**: Install the `pgvector` extension to handle vector operations.
- **Configure Connection**: Use environment variables to manage your database connection securely.

## Deployment

### Render Deployment

1. **Prepare Docker Images**: Ensure your Docker images are optimized for deployment.

2. **Set Up Render**: Follow Render's documentation to deploy your Docker-based application. Use Docker volumes to manage persistent data storage.

3. **Environment Configuration**: Use Render's environment variable settings to configure your database and application settings.

## Contributions

Contributions are welcome! Please submit a pull request or open an issue to discuss any potential changes or contributions.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For further information or questions, please contact the repository owner at briancg.lab@gmail.com.
```

### Key Considerations

- **Database Use**: The README recommends using PostgreSQL with the `pgvector` extension for structured data storage, which is more scalable and efficient than flat file storage for complex applications.
- **Docker Volumes**: Suggests using Docker volumes for managing file storage separately from the application code. This is especially useful for deployment on platforms like Render, where you want to persist data independently of your application containers.
- **Environment Variables**: Emphasizes the use of environment variables for managing sensitive information like database credentials.