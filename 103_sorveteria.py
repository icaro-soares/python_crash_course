class Restaurant:
    """Simula um restaurante"""

    def __init__(self, restaurant_name, cuisine_type):
        """Pega os atributos básicos do restaurante"""
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type.title()


    def describe_restaurant(self):
        """Mostra na tela o nome e  tipo de cozinha do restaurante"""
        print(f"Nosso restaurante se chama {self.restaurant_name}, e têm uma cozinha {self.cuisine_type}")


    def open_restaurant(self):
        """Mostra na tela que o restaurante está aberto"""
        print(f'O restaurante {self.restaurant_name} está aberto!')


class IceCreamStand(Restaurant):
    """Simula uma soreveteria"""

    def __init__(self, restaurant_name, cuisine_type):
        """Herda os atributos de Restaurant"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['baunilha', 'morango', 'chocolate']


    def describe_flavors(self):
        print('Os sabores disponíveis são: ')
        for flavor in self.flavors:
            print(f'\t{flavor.title()}')


my_ice_cream = IceCreamStand('icy', 'gelato')
my_ice_cream.describe_restaurant()
my_ice_cream.describe_flavors()
