cities = {
        'São Paulo':{
                'country':'Brasil',
                'population':12_005_878,
                'fact':'Possui a maior rede de cinemas da América Latina.',
        },
        'Tóquio':{
                'country':'Japão',
                'population':37_000_000,
                'fact':'Sua incrível eficiência e precisão no transporte público.',
        },
        'Paris':{
                'country':'França',
                'population':12_000_000,
                'fact':'Paris possui uma rede subterrânea complexa e fascinante conhecida como as Catacumbas de Paris.'
        }
}
for lugar, info in cities.items():
    print(f'Lugar: {lugar.title()}\n\t{info['country']}\n\t{info['population']}\n\t{info['fact']}')
    print('-=' * 30)
