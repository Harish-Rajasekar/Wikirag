from src.wikipedia_loader import WikipediaLoader


def main():

    loader = WikipediaLoader()

    topic = input("Enter a Wikipedia topic: ")

    try:
        article = loader.get_article(topic)

        print("\n" + "=" * 60)
        print("TITLE")
        print(article["title"])

        print("\n" + "=" * 60)
        print("SUMMARY")
        print(article["summary"][:500])

        print("\n" + "=" * 60)
        print("URL")
        print(article["url"])

    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()