pizzas = ['Mussarela', 'Marguerita', 'Calabresa']
friends_pizzas = pizzas[:]
pizzas.append('Portuguesa')
friends_pizzas.append('Marco Polo')
print('Minhas pizzas favoritas: ', end='')
for pizza in pizzas:
    print(f'[{pizza}] ', end='')
print('\nMinhas pizzas favoritas são: ', end='')
for pizza in friends_pizzas:
    print(f'[{pizza}] ', end='')
