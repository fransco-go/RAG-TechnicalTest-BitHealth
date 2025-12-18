# Refactored RAG Service

This repository contains a refactored implementation of a simple
**Retrieval-Augmented Generation (RAG)** service built with **FastAPI**,
a LangGraph-style workflow, and **Qdrant with an in-memory fallback**.

---

## Key Features

- FastAPI-based HTTP API
- Clear separation of concerns (API, services, workflow)
- Explicit dependency management
- Qdrant vector store with automatic in-memory fallback
- Deterministic fake embeddings to preserve original behavior

---

## How to Run

```bash
python -m venv venv
source venv/bin/activate  # Linux / macOS
# or
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

### Run the FastAPI server
```bash
uvicorn app.main:app --reload
```
The API will be available at: `http://localhost:8000`

### FastAPI also provides an interactive Swagger UI at:
```bash
http://localhost:8000/docs
```

### API Endpoints
* `POST /add` – Add a document to the store
* `POST /ask` – Ask a question and retrieve an answer
* `GET /status` – Check storage backend status
