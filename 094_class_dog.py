class Dog:
    """Simples tentativa de modelar um cachorro"""

    def __init__(self, name, age):
        self.name = name # recebe o nome do cachorro
        self.age = age # recebe a idade do cachorro


    def sit(self):
        """Simula o cachorro sentando"""
        print(f'{self.name} is now sitting.')

    
    def roll_over(self):
        """Simula o cachorro rolando"""
        print(f'{self.name} rolled over.')


my_dog = Dog('Ryoko', 13)
print(f'My dog name is {my_dog.name}')
print(f'My dog age is {my_dog.age}')
