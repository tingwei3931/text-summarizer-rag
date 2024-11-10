# Text Summarizer tool using RAG

This project is a text summarization application that uses LangChain and OpenAI's GPT-3.5-turbo model to generate concise summaries from large text documents. The project also includes a vector store for efficient retrieval of relevant text chunks.

## Features

-   **Text Summarization**: Generate concise summaries from large text documents.
-   **Vector Store**: Efficient retrieval of relevant text chunks using FAISS.
-   **Asynchronous Processing**: Asynchronous initialization and processing for better performance using WebSocket.

## Installation

1. Clone the repository:

    ```sh
    [git clone https://github.com/username/repository.git](https://github.com/tingwei3931/text-summarizer-rag.git)
    cd text-summarizer-rag
    ```

2. Create a virtual environment and activate it:

    ```sh
    python -m venv .venv
    source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Configuration

1. Set up your OpenAI API key:

    ```sh
    export OPENAI_API_KEY='your_openai_api_key'
    ```

## Usage

1. Start the Flask application:

    ```sh
    flask run
    ```

2. Open your web browser and navigate to `http://127.0.0.1:5000/`.

3. Enter your query in the input field and click "Summarize" to generate a summary.

## Project Structure

-   `app.py`: Main application file that initializes the Flask app and handles routes.
-   `summarizer.py`: Contains the logic for creating the RAG pipeline and generating summaries.
-   `document_store.py`: Handles loading documents, splitting text into chunks, and creating the FAISS vector store.
-   `templates/index.html`: HTML template for the web interface.
-   `.gitignore`: Specifies files and directories to be ignored by Git.
-   `requirements.txt`: Lists the Python dependencies for the project.

## Routes

-   `/`: Main route that displays the input form and summary results.
-   `/summarize`: POST route that processes the input query and generates a summary.
-   `/check_vector_store`: GET route that checks the status of the vector store (deprecated).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

-   [LangChain](https://github.com/langchain/langchain)
-   [OpenAI](https://www.openai.com/)
-   [FAISS](https://github.com/facebookresearch/faiss)
