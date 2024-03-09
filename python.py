import time
def ask_question(question):
    print("Chatbot:", question)
    time.sleep(1)
def user_reply():
    user_input = input("You: ")
    return user_input
while True:
    question = "What are you doing?"
    ask_question(question)
    user_response = user_reply()
    print("Chatbot: That's interesting. Do you enjoy your work?")
    user_response = user_reply()
    print("Chatbot: Great! Now, tell me, what purpose you doing this work?")
    user_response = user_reply()
    print("Chatbot: Thanks for sharing. This work is very important for you?")
    user_response = user_reply()
    print("Chatbot: I hope you get this internship certificate !. Is there anything else on your mind?")
    ask_question("Do you want to continue? (yes/no)")
    user_response = user_reply()
    if user_response.lower() != "yes":
        print("Chatbot: Okay, goodbye!")
        