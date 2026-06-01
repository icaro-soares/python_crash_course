idade = ' '
while idade != 999:
    if idade != 999:
        idade = int(input('Qual sua idade (quit p/ sair): '))
        if idade < 3:
            print('Entrada gratuita.')
        elif 3 <= idade < 12:
            print('O ingresso custa US$10.')
        else:
            print('O ingresso custa US$15.')
