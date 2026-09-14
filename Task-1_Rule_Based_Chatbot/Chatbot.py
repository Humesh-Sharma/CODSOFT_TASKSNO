# Rule-Based Chatbot

print("================================")
print(" Welcome to Rule-Based Chatbot ")
print("Type 'bye' to exit the chatbot.")
print("================================")

while True:
    user = input("You: ").lower()

    if user == "hello" or user == "hi":
        print("Bot: Hello! How can I help you?")

    elif user == "how are you":
        print("Bot: I am fine. Thank you for asking!")

    elif user == "what is your name":
        print("Bot: My name is ChatBot.")

    elif user == "who created you":
        print("Bot: I was created using Python programming.")

    elif user == "what can you do":
        print("Bot: I can answer simple questions based on predefined rules.")

    elif user == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand your question.")