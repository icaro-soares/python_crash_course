from random import randint

class Dice:
    """Tentativa de criar um dado"""

    def __init__(self, sides=6):
        self.sides = sides

    def roll_dice(self):
       print(f'Lado: {randint(1, self.sides)}')

dado1 = Dice()
print('10x de 6 lados')
for t in range(1, 11):
    dado1.roll_dice()
print('-=' * 30)
dado2 = Dice(10)
print('10x de 10 lados')
for t in range(1, 11):
    dado2.roll_dice()
print('-=' * 30)
dado3 = Dice(20)
print('10x de 20 lados')
for t in range(1, 21):
    dado3.roll_dice()
