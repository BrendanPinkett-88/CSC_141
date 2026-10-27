# archived messages
def archive_messages(messages, archived_messages):
    for message in messages:
        archived_messages.append(message)
    messages.clear()

text_messages = [
    "Hello, how are you?",
    "Have a great day!",
    "See you later!",
    "Good luck with your work!"
]

archived_messages = []

archive_messages(text_messages, archived_messages)

print("\nOriginal list:")
print(text_messages)

print("\nArchived messages:")
print(archived_messages)