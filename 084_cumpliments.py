def show_messages(cumpliments):
    """Mostra uma lista de cumprimentos"""
    while cumpliments:
        for cumpliment in cumpliments:
            print(f'{cumpliment.title()}')
            cumpliments.pop()

cumpliments = ['Hi!', 'Hey there, how you doing?', 'long time no see!']
show_messages(cumpliments)
