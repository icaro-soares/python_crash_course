"""Designs que precisam ser impressos"""
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron',]
completed_models = []

# Simula a impressão dos designs
# Passa a impressão para completed_models
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f'Printing model: {current_design}')
    completed_models.append(current_design)
    
# Exibe os modelos concluídos
print('\nThe following models have been printed:')
for complete in completed_models:
    print(f'\t• {complete.title()}')
