class Car:

    """Tentativa de representar um carro"""
    def __init__(self, make, model, year):
        """Inicializa os atributos para descrever o carro"""
        self.make = make
        self.model = model
        self.year = year
    

    def get_descriptive_name(self):
        """Retorna um nome descritivo, formatado elegantemente"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name


    def odometer_reading(self):
        """Exibe uma frase mostrando a quilometragem do carro em milhas"""


my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
