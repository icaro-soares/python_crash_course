class Restaurant:

    """Simula um restaurante"""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type.title()
        self.number_served = 0

    
    def describe_restaurant(self):
        """Descreve o nome do restaurante e o tipo de cozinha"""
        print(f"The restaurant {self.restaurant_name} has {self.cuisine_type} food!")

    
    def open_restaurant(self):
        """Imprime uma mensagem que o restaurante está aberto"""
        print(f"{self.restaurant_name} is now open!")
    

    def served_people(self):
        """Mostra o número de pessoas servidas"""
        print(f"Number of people served: {self.number_served}")


    def set_number_served(self, clientes):
        """Permite ao usuário colocar o número de pessoas servidas diretamente pelo programa"""
        self.number_served = clientes

    def increment_number_served(self, clientes):
        """Acrescenta um número de clientes atendidos ao valor original"""
        self.number_served += clientes


restaurant = Restaurant('la casa', 'mexican')
restaurant.open_restaurant()
restaurant.describe_restaurant()
restaurant.served_people()
restaurant.set_number_served(20)
restaurant.served_people()
restaurant.increment_number_served(15)
restaurant.served_people()
