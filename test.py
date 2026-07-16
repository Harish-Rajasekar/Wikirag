from src.wikipedia_loader import WikipediaLoader
from src.text_splitter import TextSplitter
from src.embeddings import EmbeddingGenerator
from src.vector_store import VectorStore
from src.retriever import Retriever


loader = WikipediaLoader()
splitter = TextSplitter()
embedder = EmbeddingGenerator()
store = VectorStore()

topic = input("Enter Wikipedia topic: ")

article = loader.get_article(topic)

chunks = splitter.split_text(article["content"])

embeddings = embedder.generate_embeddings(chunks)

metadata = []

for i in range(len(chunks)):
    metadata.append(
        {
            "title": article["title"],
            "url": article["url"],
            "chunk_id": i
        }
    )

store.add_documents(
    chunks,
    embeddings,
    metadata
)

print("\nDatabase Ready!")

retriever = Retriever()

query = input("\nAsk a question: ")

results = retriever.retrieve(query)
context_chunks = results["documents"][0]

from src.prompt import PromptBuilder
from src.llm import GeminiClient

prompt = PromptBuilder.build_prompt(
    context_chunks,
    query
)

llm = GeminiClient()

answer = llm.generate_answer(prompt)

print("\n")
print("=" * 80)
print("ANSWER")
print("=" * 80)
print(answer)