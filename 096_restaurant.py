class Restaurant:
    
    """Simula um restaurante"""
    def __init__(self, name, cuisine):
        """Recebe o nome e o tipo de cozinha do restaurante"""
        self.name = name.title()
        self.cuisine = cuisine.title()

    
    def describe_restaurant(self):
        """Descreve o restaurante"""
        print(f'Name: {self.name}. Cuisine: {self.cuisine}')

    
    def open_restaurant(self):
        """Mostra que o restaurante está aberto"""
        print(f'{self.name} is now open')


my_restaurant = Restaurant('montecarlo', 'mexican')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
print('-=' * 30)
your_restaurant = Restaurant('paris', 'french')
your_restaurant.describe_restaurant()
your_restaurant.open_restaurant()
print('-=' * 30)
their_restaurant = Restaurant(cuisine='brazilian', name='a bodega')
their_restaurant.describe_restaurant()
their_restaurant.open_restaurant()
