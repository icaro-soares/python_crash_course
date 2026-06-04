class Restaurant():
    
    """Simula um restaurante"""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    
    def describe_restaurant(self):
        """Descreve o restaurante em poucas palavras"""
        print(f"Name: {self.restaurant_name}. Cuisine type: {self.cuisine_type}")

    
    def open_restaurant(self):
        """Exibe uma menssagem que o restaurante está aberto"""
        print(f"The restaurant {self.restaurant_name} is now open!")


my_restaurant = Restaurant('La Cuisine', 'Italian')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
