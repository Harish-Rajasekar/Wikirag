from sentence_transformers import CrossEncoder


class Reranker:

    def __init__(self):

        self.model = CrossEncoder(
            "cross-encoder/ms-marco-MiniLM-L-6-v2"
        )

    def rerank(self, query, documents, top_k=5):

        pairs = [
            (query, doc)
            for doc in documents
        ]

        scores = self.model.predict(pairs)

        ranked = sorted(
            zip(scores, documents),
            reverse=True
        )

        return [
            doc
            for _, doc in ranked[:top_k]
        ]