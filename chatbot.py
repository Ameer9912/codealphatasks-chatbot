import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
pairs = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you?', ['I am doing well, thank you!', 'I am great! How can I assist you today?']),
    (r'what is your name?', ['I am a chatbot created by OpenAI.', 'You can call me Chatbot.']),
    (r'quit', ['Bye! Have a great day!', 'Goodbye!']),
    (r'What else?', ['Nothing much!U say something']),
    (r'(.*)', ['I am not sure how to respond to that. Can you ask something else?'])
]

# Create a chatbot instance
chatbot = Chat(pairs, reflections)

def chat():
    print("Hello! I'm a chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Chatbot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chat()
