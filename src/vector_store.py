import chromadb


class VectorStore:
    """
    Handles storing and retrieving embeddings using ChromaDB.
    """

    def __init__(self):

        self.client = chromadb.Client()

        self.collection = self.client.get_or_create_collection(
            name="wikipedia_articles"
        )

    def add_documents(self, chunks, embeddings, metadata):

        ids = [str(i) for i in range(len(chunks))]

        self.collection.add(
            ids=ids,
            documents=chunks,
            embeddings=embeddings.tolist(),
            metadatas=metadata
        )

    def search(self, query_embedding, n_results=3):

        results = self.collection.query(
            query_embeddings=[query_embedding.tolist()],
            n_results=n_results
        )

        return results