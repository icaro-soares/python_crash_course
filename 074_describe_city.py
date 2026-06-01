def describe_city(city, country='Brazil'):
    """Escreve em que país fica uma cidade"""
    print(f'{city.title()} fica no país {country.title()}')

describe_city(city='recife')
describe_city(city='salvador')
describe_city(city='new york', country='estados unidos')
