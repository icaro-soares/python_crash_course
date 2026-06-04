class Dog:
    """Simples tentativa de modelar um cachorro"""

    def __init__(self, name, age):
        self.name = name.title() # recebe o nome do cachorro
        self.age = age # recebe a idade do cachorro


    def sit(self):
        """Simula o cachorro sentando"""
        print(f'{self.name} is now sitting.')

    
    def roll_over(self):
        """Simula o cachorro rolando"""
        print(f'{self.name} rolled over.')


my_dog = Dog(age=13, name='ryoko')
print(f'My dog name is {my_dog.name}')
print(f'My dog age is {my_dog.age} years old')
my_dog.sit()
my_dog.roll_over()
