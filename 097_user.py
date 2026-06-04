class User:

    """cria um usuário"""
    def __init__(self, first_name, last_name, age, sex, country, nick):
        """Recolhe todos os dados do usuário"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.sex = sex.title()
        self.country = country.title()
        self.nick = nick


    def greet_user(self):
        print(f"Greetings, {self.nick}, we welcome you!")


    def describe_user(self):
        print(f'\nUser info:\n\tFirst Name: {self.first_name}\n\tLast Name: {self.last_name}\n\tAge: {self.age}\n\tSex: {self.sex}\n\tCountry: {self.country}\n\tNickname: {self.nick}')

    
my_user = User('ícaro', 'oliveira', 35, 'male', 'usa', '1car0')
my_user.greet_user()
my_user.describe_user()
print('-=' * 30)
her_user = User(last_name='mendes', first_name='amanda', sex='female', age=35, country='mexico', nick='ammamendes')
her_user.greet_user()
her_user.describe_user()
