from time import sleep
import os

def nome_valor():
    """Imprime cabeçalho da nota"""
    print('-' * 30)
    print(f'{'nome'.upper():<15}{'valor'.upper():>15}')
    print('-' * 30)

def subtotal(total):
    """Calcula o subtotal da nota"""
    print('-' * 30)
    print(f'{'Subtotal':<15}{total:>15.2f}')
    print('-' * 30)

def nota_fiscal():
    """Mostra o cabeçalho da nota fiscal"""
    print('-' * 30)
    print(f'{'nota fiscal'.upper():^30}')
    print('-' * 30)
    print(f'{'Nome':<15}{'Valor':>15}')
    print('-' * 30)

def desconto():
    """Mostra o rodapé do desconto"""
    print('-' * 30)
    print(f'{'Desconto':<15}{(total * 0.05):>15.2f}')
    print('-' * 30)
    print(f'{'Total':<15}{total:>15.2f}')

produtos = {}
lista_compras = []
total = 0
while True:
    produtos['prod'] = input('Produto? ').strip()
    produtos['preco'] = float(input('Preço: R$'))
    total += produtos['preco']
    lista_compras.append(produtos.copy())
    resp = ' '
    while resp not in 'sn':
        resp = input('Continuar? [s/n] ').strip().lower()
    print('-' * 30)
    if resp == 'n':
        print(f'{'Obrigado!':^30}')
        break
sleep(2)
os.system('cls' if os.name =='nt' else 'clear')
nome_valor()
for p in lista_compras:
    print(f'{p['prod'].upper():<15}{p['preco']:>15.2f}')
subtotal(total)
while True:
    forma = int(input('Forma de pagamento: [0 - cancelar compra][1 - à vista][2 - à vista no cartão][3 - parcelado até 10x] '))
    print('Forma escolhida: ', end='')
    match forma:
        case 0:
            print('anulando operação... obrigado, volte sempre!')
            sleep(2)
            quit()
            break
        case 1:
            print('à vista. Total com desconto de 5%')
            total -= (total * 0.05)
            sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        case 2:
            print('à vista no cartão. Preço normal.')
            sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        case 3:
            print('parcelado até 10x. Total com acréscimo de 20%')
            sleep(2)
            total += (total * 0.20)
            parc = int(input('Quantas parcelas? [até 10x] '))
            tot_parc = total / parc
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        case _:
            print('Opção inválida, tente novamente!')
match forma:
    case 1:
        nota_fiscal()
        for p in lista_compras:
            print(f'{p['prod']:<15}{p['preco']:>15.2f}')
        desconto()
    case 2:
        nota_fiscal()
        for p in lista_compras:
            print(f'{p['prod']:<15}{p['preco']:>15.2f}')
    case 3:
        nota_fiscal()
        for p in lista_compras:
            print(f'{p['prod']:<15}{p['preco']:>15.2f}')
        print(f'{'juros'.upper():<15}{"20%":>15.2f}')
        print('-' * 30)
        print(f'{'Total'.upper():<15}{total:>15.2f}')
        print('-' * 30)
        print(f'{parc:<15}{tot_parc:>15.2f}')
