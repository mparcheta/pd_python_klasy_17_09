class Car:

    def __init__(self, name: str, mileage: int):
        self.name = name
        self.mileage = mileage

    def description(self):
        print(f"The {self.name} has {self.mileage} miles.")

    def __str__(self):
        return f"The {self.name} has {self.mileage} miles."


blue_car = Car("blue car", 20000)
red_car = Car("red car", 30000)

# Printing content via __str__ method.
print(blue_car)
print(red_car)

# Printing content via description method.
blue_car.description()
red_car.description()