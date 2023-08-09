def simple_chatbot(user_input):
    greetings = ["hello", "hi", "hey", "howdy", "hola"]
    responses = [
        "Hello there!",
        "Hi!",
        "Hey!",
        "Howdy!",
        "Hola!",
        "Hi, how can I assist you?",
        "Hello! How's your day going?",
        "Hey there! What can I do for you?",
        "Howdy! What's on your mind?",
        "Hola! How may I help you today?"
    ]

    for word in user_input.split():
        if word.lower() in greetings:
            return responses[greetings.index(word.lower())]

    return "Sorry, I didn't quite catch that. Can you please rephrase?"

# Test the chatbot
while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Chatbot: Goodbye!")
        break
    else:
        response = simple_chatbot(user_input)
        print("Chatbot:", response)
