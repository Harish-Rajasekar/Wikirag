from src.embeddings import EmbeddingGenerator
from src.vector_store import VectorStore


class Retriever:
    """
    Retrieves relevant document chunks for a user query.
    """

    def __init__(self):

        self.embedder = EmbeddingGenerator()
        self.vector_store = VectorStore()

    def retrieve(self, query: str, n_results: int = 3):

        query_embedding = self.embedder.generate_embeddings([query])[0]

        results = self.vector_store.search(
            query_embedding,
            n_results=n_results
        )

        return results