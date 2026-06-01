sanduiches = ['atum', 'pastrami', 'misto', 'pastrami', 'pastrami', 'americano']
print('Cardápio')
for sanduiche in sanduiches:
    print(f'\t{sanduiche.title()}')
print('A lanchonete está sem sanduíche de pastrami')
while 'pastrami' in sanduiches:
    sanduiches.remove('pastrami')
print('\nNovo cardápio')
for sanduiche in sanduiches:
    print(f'\t{sanduiche.title()}')