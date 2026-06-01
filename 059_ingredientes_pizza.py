ingrediente = ' '
while ingrediente != 'quit':
    if ingrediente != 'quit':
        ingrediente = input('Qual ingrediente deseja adicionar a pizza? ')
        print(f'{ingrediente.title()} adicionado(a) com sucesso!')
    else:
        print('Saindo...')
