import os
from groq import Groq
from dotenv import load_dotenv


class LLMClient:
    """
    Handles communication with Groq LLMs.
    """

    def __init__(self):

        load_dotenv()

        api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            raise ValueError("GROQ_API_KEY not found in .env")

        self.client = Groq(api_key=api_key)

        self.model = "llama-3.3-70b-versatile"

    def generate_answer(self, prompt):

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.2,
        )

        return response.choices[0].message.content