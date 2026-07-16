from sentence_transformers import SentenceTransformer


class EmbeddingGenerator:
    """
    Generates embeddings for text chunks using Sentence Transformers.
    """

    def __init__(self):
        """
        Load the embedding model once.
        """

        self.model = SentenceTransformer(
            "sentence-transformers/all-MiniLM-L6-v2"
        )

    def generate_embeddings(self, chunks: list):
        """
        Generate embeddings for a list of chunks.

        Args:
            chunks (list): List of text chunks.

        Returns:
            embeddings
        """

        embeddings = self.model.encode(
            chunks,
            convert_to_numpy=True,
            show_progress_bar=True
        )

        return embeddings