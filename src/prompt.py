class PromptBuilder:
    """
    Builds prompts for the LLM using retrieved context and chat history.
    """

    @staticmethod
    def build_prompt(context_chunks, question, chat_history=None):

        context = "\n\n".join(context_chunks)

        history = ""

        if chat_history:
            history = "\n".join(
                [
                    f"User: {msg['user']}\nAssistant: {msg['assistant']}"
                    for msg in chat_history
                ]
            )

        prompt = f"""
You are an AI assistant answering questions about the currently loaded Wikipedia article.

Use ONLY the provided context to answer the question.

The previous conversation is provided to help understand follow-up questions such as
"he", "they", "that team", etc.

If the answer is not available in the context, say:

"I couldn't find that information in the provided Wikipedia article."

----------------------------
Previous Conversation
----------------------------

{history}

----------------------------
Context
----------------------------

{context}

----------------------------
Current Question
----------------------------

{question}

----------------------------
Answer
----------------------------
"""

        return prompt