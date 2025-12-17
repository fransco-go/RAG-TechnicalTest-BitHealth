from fastapi import FastAPI
from app.api import router

app = FastAPI(title="Learning RAG Demo")
app.include_router(router)