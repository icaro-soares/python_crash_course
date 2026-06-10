class User:
    """Simula uma tentativa de login"""

    def __init__(self, first_name, last_name, age, location):
        """Coleta os dados do usuário"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        """Faz um descrição rápida dos dados do usuário"""
        print(f'User info:\n\tFirst name: {self.first_name}\n\tLast name: {self.last_name}\n\tAge: {self.age}\n\tLocation: {self.location}')

    def greet_user(self):
        """Exibe uma mensagem de boas vindas"""
        print(f'Bem vindo(a), {self.first_name}')

    def increment_login_attempts(self):
        """Incrementa em 1 o número de tentativas de login"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reseta o número de tentativas de login"""
        self.login_attempts = 0

    def show_login_attempts(self):
        """Mostra o número de tentativas de login"""
        print(f'Tentativas de login: {self.login_attempts}')

class Admin(User):
    """Simula os dados do administrador"""

    def __init__(self, first_name, last_name, age, location):
        """
        Captura os dados, e logo depois cria uma lista de privilégios exclusivos.
        """
        super().__init__(first_name, last_name, age, location)
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        """Mostra a lista de privilégios do administrador"""
        print('Privilégios de admin:')
        for privilege in self.privileges:
            print(f'\t{privilege.capitalize()}')

my_user = Admin('joão', 'romão', 40, 'paraíba')
my_user.greet_user()
my_user.describe_user()
my_user.show_privileges()
