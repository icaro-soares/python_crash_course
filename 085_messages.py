def send_messages(send, sent):
    while send:
        sent_messages = send.pop()
        print(f'Someone says: {sent_messages.title()}')
        sent.append(sent_messages)
            

messages = ['nice to meet you!', "Hi I'm pleasured to meet you", 'good bye']
sent_messages = []
send_messages(messages, sent_messages)
print(f'Messages: {messages}')
print(f'Sent messages: {sent_messages}')
