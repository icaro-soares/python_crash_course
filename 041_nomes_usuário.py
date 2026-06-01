nomes_usuario = ['admin', 'gatinho07', 'luci_doce', 'destr0ier', 'pudding']
for nome_usuario in nomes_usuario:
    if nome_usuario == 'admin':
        print('Olá administrador, gostaria de ver um relatório de status?')
    else:
        print(f'Seja bem vindo(a), {nome_usuario}, obrigado por fazer login novamente!')
