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

print("\nRetrieved Chunks:\n")

for i, doc in enumerate(results["documents"][0], start=1):

    print("=" * 80)
    print(f"Chunk {i}")
    print("=" * 80)
    print(doc[:500])
    print()