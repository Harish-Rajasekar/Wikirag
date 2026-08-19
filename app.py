from src.rag_pipeline import RAGPipeline


def main():

    rag = RAGPipeline()

    topic = input("Enter Wikipedia Topic: ")

    rag.load_topic(topic)

    while True:

        question = input("\nAsk a question (type 'exit' to quit): ")

        if question.lower() == "exit":
            break

        answer = rag.ask(question)

        print("\n" + "=" * 80)
        print("ANSWER")
        print("=" * 80)
        print(answer)


if __name__ == "__main__":
    main()