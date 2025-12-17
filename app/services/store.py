from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct, VectorParams, Distance

class DocumentStore:
    """
    Handles document storage and retrieval.
    Uses Qdrant if available, otherwise falls back to in-memory storage.
    """
    def __init__(self, embedding_service):
        self.embedding = embedding_service
        self.docs_memory = []
        self.using_qdrant = False
        self._init_qdrant()

    def _init_qdrant(self):
        try:
            self.qdrant = QdrantClient("http://localhost:6333")
            self.qdrant.recreate_collection(
                collection_name="demo_collection",
                vectors_config=VectorParams(size=self.embedding.dim, distance=Distance.COSINE)
            )
            self.using_qdrant = True
        except Exception:
            # Qdrant not available; operate in in-memory mode
            self.qdrant = None

    def add(self, text: str) -> int:
        emb = self.embedding.embed(text)
        doc_id = len(self.docs_memory)
        payload = {"text": text}

        if self.using_qdrant:
            self.qdrant.upsert(
                collection_name="demo_collection",
                points=[PointStruct(id=doc_id, vector=emb, payload=payload)]
            )
        else:
            self.docs_memory.append(text)

        return doc_id

    def search(self, query: str, limit: int = 2) -> list[str]:
        emb = self.embedding.embed(query)
        results = []

        if self.using_qdrant:
            hits = self.qdrant.search(
                collection_name="demo_collection",
                query_vector=emb,
                limit=limit
            )
            results = [hit.payload["text"] for hit in hits]
        else:
            for doc in self.docs_memory:
                if query.lower() in doc.lower():
                    results.append(doc)
            if not results and self.docs_memory:
                results = [self.docs_memory[0]]

        return results

    def status(self):
        return {
            "qdrant_ready": self.using_qdrant,
            "in_memory_docs_count": len(self.docs_memory)
        }