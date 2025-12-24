class Car:
    """
    A simple Car class with make, model, and year attributes.
    """

    # Initialize the attributes
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    # Method to describe the car
    def describe_car(self):
        print(f"{self.year} {self.make} {self.model}")



# Create a Car object
my_car = Car("Toyota", "Corolla", 2020)

# Call the describe_car method
my_car.describe_car()   # Output: 2020 Toyota Corolla
