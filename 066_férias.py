lugares = {}
while True:
    nome = input('Qual seu nome? ')
    lugar = input('Se pudesse visitar um lugar do mundo, para onde iria? ')
    lugares[nome] = lugar
    resp = input('Quer continuar? (y/n) ')
    if resp == 'n':
        break
print('\n--- Poll ---')
for nome, lugar in lugares.items():
    print(f'{nome.title()} gostaria de visitar {lugar.title()}')
    