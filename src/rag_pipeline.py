from src.wikipedia_loader import WikipediaLoader
from src.text_splitter import TextSplitter
from src.embeddings import EmbeddingGenerator
from src.vector_store import VectorStore
from src.hybrid_retriever import HybridRetriever
from src.prompt import PromptBuilder
from src.llm import LLMClient


class RAGPipeline:

    def __init__(self):

        self.loader = WikipediaLoader()
        self.splitter = TextSplitter()
        self.embedder = EmbeddingGenerator()
        self.vector_store = VectorStore()
        self.retriever = HybridRetriever(self.vector_store)
        self.llm = LLMClient()

        self.current_topic = None

    def load_topic(self, topic):

        self.vector_store.clear_collection()

        article = self.loader.get_article(topic)

        chunks = self.splitter.split_text(article["content"])

        embeddings = self.embedder.generate_embeddings(chunks)

        metadata = []

        for i in range(len(chunks)):
            metadata.append(
                {
                    "title": article["title"],
                    "url": article["url"],
                    "chunk_id": i
                }
            )

        self.vector_store.add_documents(
            chunks,
            embeddings,
            metadata
        )

        self.current_topic = topic

        print(f"\nLoaded '{topic}' successfully!")

    def ask(self, question, chat_history=None):

        if self.current_topic is None:
            raise ValueError("Load a topic first.")

        context = self.retriever.retrieve(question)

        prompt = PromptBuilder.build_prompt(
            context,
            question,
            chat_history
        )

        answer = self.llm.generate_answer(prompt)

        return answer