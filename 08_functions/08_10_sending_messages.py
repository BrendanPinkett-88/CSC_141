#sending messages
def send_messages(messages):
    for message in messages:
        print(message)

text_messages = [
    "Hello, how are you?",
    "Have a great day!",
    "See you later!",
    "Good luck with your work!"
]

sent_messages = []
send_messages(text_messages, sent_messages)

print("\nOriginal list:")
print(text_messages)

print("\nSent messages:")
print(sent_messages)