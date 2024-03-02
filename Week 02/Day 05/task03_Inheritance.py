class Vehicle:
    def __init__(self, make, model, year, fuel_type):
        self.make = make
        self.model = model
        self.year = year
        self.fuel_type = fuel_type

    def display_info(self):
        print("Make:", self.make)
        print("Model:", self.model)
        print("Year:", self.year)
        print("Fuel Type:", self.fuel_type)


class Car(Vehicle):
    def __init__(self, make, model, year, fuel_type):
        super().__init__(make, model, year, fuel_type)


class Truck(Vehicle):
    def __init__(self, make, model, year, fuel_type):
        super().__init__(make, model, year, fuel_type)


class ElectricCar(Car):
    def __init__(self, make, model, year, fuel_type, battery_capacity):
        super().__init__(make, model, year, fuel_type)
        self.battery_capacity = battery_capacity

    def display_info(self):
        super().display_info()
        print("Battery Capacity (kWh):", self.battery_capacity)


class HybridTruck(Truck):
    def __init__(self, make, model, year, fuel_type, electric_motor_power):
        super().__init__(make, model, year, fuel_type)
        self.electric_motor_power = electric_motor_power

    def display_info(self):
        super().display_info()
        print("Electric Motor Power:", self.electric_motor_power)


# Demonstration
car = ElectricCar(make="Tesla", model="Model S", year=2022, fuel_type="Electric", battery_capacity=100)
car.display_info()

truck = HybridTruck(make="Toyota", model="Tacoma", year=2023, fuel_type="Hybrid", electric_motor_power="100 kW")
truck.display_info()
