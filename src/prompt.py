class PromptBuilder:
    """
    Builds prompts for the LLM using retrieved context.
    """

    @staticmethod
    def build_prompt(context_chunks, question):
        """
        Create a prompt using the retrieved chunks and user question.
        """

        context = "\n\n".join(context_chunks)

        prompt = f"""
You are an AI assistant.

Answer ONLY using the context provided below.

If the answer is not present in the context, say:
"I couldn't find that information in the provided Wikipedia article."

----------------------------
Context
----------------------------

{context}

----------------------------
Question
----------------------------

{question}

----------------------------
Answer
----------------------------
"""

        return prompt