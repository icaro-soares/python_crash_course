def calcular_media(n1=0, n2=0):
    m = (n1 + n2) / 2
    return m

dados = {}
boletim = []
while True:
    dados['nome'] = input('Nome: ')
    dados['n1'] = float(input('AV1: '))
    dados['n2'] = float(input('AV2: '))
    dados['m'] = calcular_media(dados['n1'], dados['n2'])
    boletim.append(dados.copy())
    r = ' '
    while r not in 'SsNn':
        r = input('Quer continuar? [s/n] ')
    if r in 'Nn':
        break
print('-=' * 30)
print(f'{"Aluno":<20}{"Média":>10}')
print('-'*30)
for aluno in boletim:
    print(f'{aluno['nome'].title():<20}{aluno['m']:>10.1f}')
