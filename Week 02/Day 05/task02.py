class Car:
    def __init__(self, window, door, fuel_type):
        self.window = window
        self.door = door
        self.fuel_type = fuel_type

class Maruti(Car):
    def __init__(self, window, door, fuel_type, speed):
        super().__init__(window, door, fuel_type)
        self.speed = speed

    def display(self):
        print("Window:", self.window)
        print("Door:", self.door)
        print("Fuel Type:", self.fuel_type)
        print("Speed:", self.speed)

maruti = Maruti(window=4, door=4, fuel_type="Petrol", speed=120)
maruti.display()
