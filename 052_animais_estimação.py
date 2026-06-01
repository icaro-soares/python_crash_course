cachorro = {
        'tipo':'cachorro',
        'dono':'joão',
}
gato = {
        'tipo':'gato',
        'dono':'maria',
}
peixe = {
        'tipo':'peixe',
        'dono':'josé',
}
pets = [cachorro, gato, peixe]
for a in pets:
    print(f'Tipo: {a['tipo']}\nDono: {a['dono'].title()}')
    print('-=' * 30)
