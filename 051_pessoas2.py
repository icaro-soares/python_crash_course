icaro = {
        'first_name':'Ícaro',
        'last_name':'Calado',
        'age':30,
        'city':'Recife',
}
maria = {
        'first_name':'Maria',
        'last_name':'Oliveira',
        'age':86,
        'city':'Alagoas',
}
geneci = {
        'first_name':'Geneci',
        'last_name':'Calado',
        'age':63,
        'city':'Garanhuns',
}
people = [
        icaro, maria, geneci
]
for p in people:
    print(f'First name: {p['first_name']}\nLast name: {p['last_name']}\nAge: {p['age']}\nCity: {p['city']}')
    print('-=' * 30)
