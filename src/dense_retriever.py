from src.embeddings import EmbeddingGenerator


class Retriever:

    def __init__(self, vector_store):

        self.embedder = EmbeddingGenerator()
        self.vector_store = vector_store

    def retrieve(self, query: str, n_results: int = 8):

        query_embedding = self.embedder.generate_embeddings([query])[0]

        results = self.vector_store.search(
            query_embedding,
            n_results=n_results
        )

        return results