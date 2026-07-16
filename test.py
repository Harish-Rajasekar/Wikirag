from src.wikipedia_loader import WikipediaLoader
from src.text_splitter import TextSplitter
from src.embeddings import EmbeddingGenerator


def main():

    loader = WikipediaLoader()
    splitter = TextSplitter()
    embedder = EmbeddingGenerator()

    topic = input("Enter a Wikipedia topic: ")

    article = loader.get_article(topic)

    chunks = splitter.split_text(article["content"])

    embeddings = embedder.generate_embeddings(chunks)

    print("\nTotal Chunks :", len(chunks))
    print("Embedding Shape :", embeddings.shape)

    print("\nFirst Chunk:\n")
    print(chunks[0][:300])

    print("\nFirst Embedding (First 10 Values):\n")
    print(embeddings[0][:10])


if __name__ == "__main__":
    main()