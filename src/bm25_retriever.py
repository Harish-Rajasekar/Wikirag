from rank_bm25 import BM25Okapi
import re


class BM25Retriever:

    def __init__(self, vector_store):

        self.vector_store = vector_store
        self.bm25 = None
        self.documents = []

    def tokenize(self, text):
        text = text.lower()
        return re.findall(r"\w+", text)

    def build_index(self):

        collection = self.vector_store.collection

        data = collection.get(include=["documents"])

        self.documents = data["documents"]

        tokenized_docs = [
            self.tokenize(doc)
            for doc in self.documents
        ]

        self.bm25 = BM25Okapi(tokenized_docs)

    def retrieve(self, query, top_k=10):

        if self.bm25 is None:
            self.build_index()

        tokenized_query = self.tokenize(query)

        scores = self.bm25.get_scores(tokenized_query)

        ranked = sorted(
            zip(scores, self.documents),
            reverse=True
        )

        return [
            doc
            for _, doc in ranked[:top_k]
        ]