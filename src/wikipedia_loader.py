import wikipediaapi


class WikipediaLoader:
    """
    A class to fetch Wikipedia articles using the Wikipedia API.
    """

    def __init__(self):
        """
        Initialize the Wikipedia API client.
        """

        self.wiki = wikipediaapi.Wikipedia(
            language="en",
            user_agent="WikiRAG/1.0"
        )

    def get_article(self, topic: str) -> dict:
        """
        Fetch a Wikipedia article.

        Args:
            topic (str): Wikipedia topic.

        Returns:
            dict: Article details.
        """

        page = self.wiki.page(topic)

        if not page.exists():
            raise ValueError(f"No Wikipedia page found for '{topic}'")

        return {
            "title": page.title,
            "summary": page.summary,
            "content": page.text,
            "url": page.fullurl
        }