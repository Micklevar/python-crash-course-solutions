# 8-11. Archived Messages:

messages = ["hello", "i am batman", "we are venom"]
sent_messages = []

def show_messages(texts):
    """show a set of messages"""

    for text in texts:
        messages.pop(text)
        
        print(text)


def send_messages(messages_list, sent):

    while messages_list:
        current_message = messages_list.pop()
        print(f"Message sent: {current_message}")
        sent.append(current_message)

send_messages(messages[:], sent_messages)

print(f"Original list: {messages}")
print(f"Copy list: {messages}")
print(f"\n{sent_messages}")