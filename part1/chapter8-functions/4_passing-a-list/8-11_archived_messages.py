"""
Start with your work from Exercise 8-10. Call the func-
tion send_messages() with a copy of the list of messages. After calling the func-
tion, print both of your lists to show that the original list has retained its messages.
"""


def send_messages(messages):
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)


messages = ["Hello!", "How are you?", "Whats your name?"]
sent_messages = []
send_messages(messages[:])
print(sent_messages)
print(messages)
