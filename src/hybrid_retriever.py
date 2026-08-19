from src.dense_retriever import Retriever
from src.bm25_retriever import BM25Retriever
from src.reranker import Reranker

class HybridRetriever:

    def __init__(self, vector_store):

        self.dense = Retriever(vector_store)
        self.bm25 = BM25Retriever(vector_store)
        self.reranker = Reranker()

    def retrieve(self, question):

        dense_results = self.dense.retrieve(question)

        dense_docs = dense_results["documents"][0]

        bm25_docs = self.bm25.retrieve(question)

        merged = []

        seen = set()

        for doc in dense_docs + bm25_docs:

            if doc not in seen:

                merged.append(doc)

                seen.add(doc)

        reranked = self.reranker.rerank(
            query=question,
            documents=merged,
            top_k=5
        )

        return reranked