def archived_messages(send, sent):
    while send:
        sending = send.pop()
        print(f'Sending message: {sending.title()}')
        sent.append(sending)

send = ['hi', 'good bye', 'thank you', 'hello']
sent = []
archived_messages(send[:], sent)
print(f'Send original: {send}')
print(f'Sent: {sent}')
