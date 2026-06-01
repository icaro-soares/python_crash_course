def print_models(unprinted_models, completed_models):
    while unprinted_models:
        """Simula a impressão de modelos em 3D"""
        current_design = unprinted_models.pop()
        print(f'Printing model: {current_design}')
        completed_models.append(current_design)

def show_completed(completed_models):
    """Mostra os modelos impressos"""
    print('\nPrinted models:')
    for completed in completed_models:
        print(f'\t• {completed.title()}')

unprinted_models = ['shoes', 'gloves', 'earrings', 'necklace', 'ring']
completed_models = []
print_models(unprinted_models, completed_models)
show_completed(completed_models)
