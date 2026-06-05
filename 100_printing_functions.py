def printing_functions(unprinted_functions, printed_functions):
    """A função recebe uma lista com funções a serem impressas na tela"""
    while unprinted_functions:
        current_function = unprinted_functions.pop()
        print(f'Printing: {current_function}')
        printed_functions.append(current_function)

    
def printed_functions(printed_functions):
    """Mostra as funções impressas na tela"""
    print('\nPrinted functions:')
    for printed in printed_functions:
        print(f'\t{printed.title()}')


unprinted = ['math', 'sleep', 'datetime']   
printed = []
printing_functions(unprinted, printed)
printed_functions(printed)
