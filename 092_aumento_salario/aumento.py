import funcao_aumento


nome = input('Nome: ').strip()
sal = float(input('Salário: R$'))
print(f'\nEmpregado(a): {nome.title()}\nSalário atual: R${sal:.2f}'.replace('.', ','))
print('-=' * 30)
novo_sal = funcao_aumento.reajuste(sal)
print(f'Salário com reajuste: R${novo_sal:.2f}'.replace('.', ','))
