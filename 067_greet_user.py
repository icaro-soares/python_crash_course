def greet_user(name='<unknown>'):
    """Exibe um cumprimento simples"""
    print(f'Hello, nice to meet you, {name}')


name = input("What's your name: ")
greet_user(name)
