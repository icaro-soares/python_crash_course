sal = float(input('Qual seu salário: R$'))
if sal <= 2_431.50:
    novo_sal = sal + (sal * 0.15)
else:
    novo_sal = sal + (sal * 0.05)
print(f'Seu novo salário é de R${novo_sal:.2f}'.replace(',', '.'))
