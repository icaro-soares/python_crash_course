class User:

    """cria um usuário"""
    def __init__(self, first_name, last_name, age, sex, country):
        """Recolhe todos os dados do usuário"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.sex = sex.upper()
        self.country = country.title()


    def describe_user(self):
        print(f'User info:\n\tFirst Name: {self.first_name}\n\tLast Name: {self.last_name}\n\tAge: {self.age}\n\tSex: {self.sex}\n\tCountry: {self.country}')

    
my_user = User('ícaro', 'oliveira', 35, 'male', 'usa')
my_user.describe_user()
