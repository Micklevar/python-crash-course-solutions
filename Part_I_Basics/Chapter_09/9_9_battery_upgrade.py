# 9-9. Battery Upgrade:

class Car:
    """ A simple attempt to represent a car. """

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        """Increment odometer"""
        self.odometer_reading += miles

class Battery():
    """Represent a Battery of a electric car."""

    def __init__(self, battery_size=40):
        """Initialize the battery's attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-KWh battery.")
    
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        
        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        """Upgrade capacity of battery to 65 KWh"""
        if self.battery_size < 65:
            self.battery_size = 65

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize atributtes of the parent class."""
        super().__init__(make, model, year)
        self.battery = Battery(40)

# Intance of ElectricCar class to create a object 'first_electric_car'

first_electric_car = ElectricCar('bmw', '325i', 2012)

first_electric_car.battery.describe_battery()
first_electric_car.battery.get_range()

first_electric_car.battery.upgrade_battery()
first_electric_car.battery.describe_battery()
first_electric_car.battery.get_range()