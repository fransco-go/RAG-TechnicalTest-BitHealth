# Refactored RAG Service

This repository contains a refactored implementation of a simple
**Retrieval-Augmented Generation (RAG)** service built with **FastAPI**,
a LangGraph-style workflow, and **Qdrant with an in-memory fallback**.

The purpose of this project is **not to add new features**, but to improve
**code structure, readability, and maintainability** while preserving the
original behavior provided in the exercise.

---

## Key Features

- FastAPI-based HTTP API
- Clear separation of concerns (API, services, workflow)
- Explicit dependency management (no global state)
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
uvicorn app.main:app --reload
```

### The API will be available at:

```bash
http://localhost:8000
```

### FastAPI also provides an interactive Swagger UI at:

```bash
http://localhost:8000/docs
```
