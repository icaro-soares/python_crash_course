class Car:
    """Tentativa de representar um carro"""

    def __init__(self, make, model, year):
        """Captura dados básicos de um carro"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Retorna os dados de maneira limpa"""
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name
    
    def read_odometer(self):
        """Retorna o valor mostrado no hodômetro"""
        print*f"This car has {self.odometer_reading} miles on it."

    def update_odometer(self, mileage):
        """Atualiza o valor do hodômetro se o valor for maior ou igual"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Adiciona quantidade de milhas ao hodômetro"""
        self.odometer_reading += miles

class ElectricCar(Car):
    """Tentativa de representar um carro elétrico"""

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 40

    def show_battery_size(self):
        print(f"This car has a battery sized {self.battery_size}")

my_car = Car('volkswagen', 'polo', 2021)
print(my_car.get_descriptive_name())
print('-=' * 30)
electric_car = ElectricCar('volkswagen', 'gol', 2026)
print(electric_car.get_descriptive_name())
electric_car.show_battery_size()
