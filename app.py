from flask import Flask, render_template, request, jsonify
from document_store import initialize_vector_store
from summarizer import summarize_with_rag, create_rag_pipeline
from pathlib import Path
import asyncio
import threading
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
vector_store = None
vector_store_ready = False 

# Function to initialize the vector store asynchronously
async def initialize_vector_store_task():
    global vector_store, vector_store_ready
    vector_store = await initialize_vector_store()
    vector_store_ready = True

# Function to run the async initialization in the background
def start_vector_store_task():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(initialize_vector_store_task())


with app.app_context():
    print("Loading vector store...")
    # Start a background thread to initialize the vector store when Flask is ready to handle requests
    threading.Thread(target=start_vector_store_task).start()

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html", vector_store_ready=vector_store_ready)

@app.route("/summarize", methods=["POST"])
def summarize():
    query = request.form.get("query")
    summary = "No summary available"
    if query:
        summary = summarize_with_rag(query, vector_store)
    return render_template("index.html", vector_store_ready=True, summary=summary)

@app.route("/check_vector_store")
def check_vector_store():
    return jsonify({"ready": vector_store_ready})

if __name__ == "__main__":
    app.run(debug=True)
