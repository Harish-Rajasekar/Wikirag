from src.wikipedia_loader import WikipediaLoader
from src.text_splitter import TextSplitter


def main():

    loader = WikipediaLoader()
    splitter = TextSplitter()

    topic = input("Enter a Wikipedia topic: ")

    try:
        article = loader.get_article(topic)

        chunks = splitter.split_text(article["content"])

        print(f"\nTotal Chunks: {len(chunks)}")

        print("\n" + "=" * 60)
        print("FIRST CHUNK")
        print("=" * 60)
        print(chunks[0])

        print("\n" + "=" * 60)
        print("SECOND CHUNK")
        print("=" * 60)
        print(chunks[1])

    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()