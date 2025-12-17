import time
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.embedding import FakeEmbeddingService
from app.services.store import DocumentStore
from app.services.workflow import RagWorkflow

router = APIRouter()

embedding = FakeEmbeddingService(dim=128)
store = DocumentStore(embedding)
workflow = RagWorkflow(store)

class QuestionRequest(BaseModel):
    question: str

class DocumentRequest(BaseModel):
    text: str

@router.post("/ask")
def ask_question(req: QuestionRequest):
    start = time.time()
    try:
        result = workflow.run(req.question)
        return {
            "question": req.question,
            "answer": result.answer,
            "context_used": result.context,
            "latency_sec": round(time.time() - start, 3)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/add")
def add_document(req: DocumentRequest):
    try:
        doc_id = store.add(req.text)
        return {"id": doc_id, "status": "added"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/status")
def status():
    return store.status()