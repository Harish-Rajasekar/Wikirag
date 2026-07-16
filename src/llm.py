import os
from dotenv import load_dotenv
from google import genai


class GeminiClient:
    """
    Handles communication with Google's Gemini models.
    """

    def __init__(self):

        load_dotenv()

        api_key = os.getenv("GOOGLE_API_KEY")

        if not api_key:
            raise ValueError("GOOGLE_API_KEY not found.")

        self.client = genai.Client(api_key=api_key)

    def generate_answer(self, prompt: str):

        response = self.client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        return response.text