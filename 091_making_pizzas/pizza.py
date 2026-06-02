def make_pizza(size, *toppings):
    """Recebe o tamanho e os acompanhamentos da pizza"""
    print(f'\nMaking a {size}-inch pizza with the follwing toppings:')
    for topping in toppings:
        print(f'\t- {topping}')
        