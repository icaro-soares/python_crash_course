favorite_places = {
        'ana':{
                'primeiro':'boa viagem',
                'segundo':'carneiros',
                'terceiro':'porto de galinhas',
        },
        'maria':{
                'primeiro':'itamaracá',
                'segundo':'jampa',
                'terceiro':'phuket',
        },
        'joão':{
                'primeiro':'frança',
                'segundo':'japão',
                'terceiro':'islândia'
        },
}
for pessoa, lugar in favorite_places.items():
    print(f'{pessoa.title()} gosta de {lugar['primeiro'].title()}, {lugar['segundo'].title()}, {lugar['terceiro'].title()}')
    