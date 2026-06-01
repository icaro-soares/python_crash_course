def city_country(city='Santiago', country='Chile'):
    """Imprime o nome de uma cidade e seu país"""
    if city == '':
        city = 'Santiago'
    if country == '':
        country = 'Chile'
    print(f'"{city}", "{country}"')

city_country('Recife', 'Brasil')
city_country('Nevada', 'Estados Unidos')
city_country()
cidade = input('Cidade: ').strip().capitalize()
país = input('País: ').strip().capitalize()
city_country(city=cidade, country=país)
