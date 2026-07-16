from langchain_text_splitters import RecursiveCharacterTextSplitter


class TextSplitter:
    """
    Splits large documents into smaller overlapping chunks.
    """

    def __init__(self):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len,
            is_separator_regex=False,
        )

    def split_text(self, text: str):
        """
        Split text into chunks.

        Args:
            text: The complete article text.

        Returns:
            List of text chunks.
        """
        return self.splitter.split_text(text)