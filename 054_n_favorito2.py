números_favoritos = {
        'ana':{
                'n1':7,
                'n2':52,
                'n3':48,
        },
        'bia':{
                'n1':96,
                'n2':34,
                'n3':24,
        },
        'josé':{
                'n1':7,
                'n2':100,
                'n3':125,
        },
}
for pessoa, núm in números_favoritos.items():
    print(f'{pessoa.title()} têm os números favoritos: {núm['n1']}, {núm['n2']}, {núm['n3']}.')
