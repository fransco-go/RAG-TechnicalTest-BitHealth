import random

class FakeEmbeddingService:
    """
    Deterministic fake embedding used to preserve original behavior
    """
    def __init__(self, dim: int = 128):
        self.dim = dim

    def embed(self, text: str) -> list[float]:
        # Seed based on input so it's "deterministic"
        random.seed(abs(hash(text)) % 10000)
        return [random.random() for _ in range(self.dim)]