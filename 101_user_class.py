class User:
    """Classe que simula o login de usuário"""

    def __init__(self, first_name, last_name, nickname):
        """Captura os dados do first_name, last_name e nickname do usuário"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.nickname = nickname
        self.login_attempts = 0

    def describe_user(self):
        """Imprime as informações básicas do usuário"""
        print(f"Name: {self.first_name}\nLast name: {self.last_name}\nNickname: {self.nickname}")

    def greet_user(self):
        """Imprime um cumprimento para o usuário"""
        print(f'\nSeja bem vindo(a), {self.nickname}!')

    def show_login_attempts(self):
        """Imprime o número de tentativas de login na tela"""
        print(f"Tentativas de login: {self.login_attempts}")

    def increment_login_attempts(self):
        """Faz o incremento de 1 na tentativa de login"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reseta as tentativas de login"""
        self.login_attempts = 0

my_user = User('andré', 'calaça', 'andre1')
my_user.describe_user()
my_user.greet_user()
my_user.show_login_attempts()
my_user.increment_login_attempts()
my_user.show_login_attempts()
my_user.reset_login_attempts()
my_user.show_login_attempts()
