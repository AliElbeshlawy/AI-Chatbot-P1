def chatbot():
    print("🤖 Welcome! Type 'exit' to quit.")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input in ["exit", "quit", "bye"]:
            print("Bot: Goodbye! 👋")
            break

        elif user_input in ["hello", "hi", "hey"]:
            print("Bot: Hello! How can I help you?")

        elif "your name" in user_input:
            print("Bot: I am a simple chatbot 🤖")

        elif "help" in user_input:
            print("Bot: Try saying hello or ask for time.")

        elif "time" in user_input:
            import datetime
            now = datetime.datetime.now()
            print(f"Bot: Time is {now.strftime('%H:%M:%S')}")

        else:
            print("Bot: I don't understand.")

if __name__ == "__main__":
    chatbot()