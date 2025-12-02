"""
Car Class Module
Demonstrates creating a class in a module
"""


class Car:
    """
    A simple Car class to demonstrate OOP in modules
    """

    # Class variable (shared by all instances)
    total_cars = 0

    def __init__(self, brand, model, year):
        """Initialize a new Car"""
        self.brand = brand
        self.model = model
        self.year = year
        self.odometer = 0
        Car.total_cars += 1

    def get_info(self):
        """Return formatted car information"""
        return f"{self.year} {self.brand} {self.model}"

    def drive(self, miles):
        """Add miles to odometer"""
        self.odometer += miles
        return f"Drove {miles} miles. Total: {self.odometer} miles"

    def honk(self):
        """Make the car honk"""
        return f"{self.brand} goes beep beep! 🚗"

    def get_age(self, current_year=2025):
        """Calculate car's age"""
        return current_year - self.year

    def __str__(self):
        """String representation of the car"""
        return self.get_info()

    def __repr__(self):
        """Developer-friendly representation"""
        return f"Car('{self.brand}', '{self.model}', {self.year})"

    @classmethod
    def get_total_cars(cls):
        """Get total number of cars created"""
        return cls.total_cars


class ElectricCar(Car):
    """
    Electric Car class - inherits from Car
    """

    def __init__(self, brand, model, year, battery_size):
        """Initialize an electric car"""
        super().__init__(brand, model, year)
        self.battery_size = battery_size
        self.battery_level = 100  # Percentage

    def charge(self):
        """Charge the battery to 100%"""
        self.battery_level = 100
        return f"{self.brand} {self.model} is fully charged! 🔋"

    def get_range(self):
        """Estimate range based on battery"""
        range_per_kwh = 4  # miles per kWh
        return self.battery_size * range_per_kwh

    def get_info(self):
        """Override to include battery info"""
        base_info = super().get_info()
        return f"{base_info} (Electric, {self.battery_size}kWh battery)"


# Module metadata
__version__ = "1.0.0"
__author__ = "Python Series"


# Test code (runs only when executed directly)
if __name__ == "__main__":
    print("🚗 Car Module - Testing")
    print()

    # Create regular car
    car1 = Car("Toyota", "Camry", 2022)
    print(f"Created: {car1.get_info()}")
    print(car1.drive(100))
    print(car1.honk())
    print(f"Car age: {car1.get_age()} years")
    print()

    # Create electric car
    car2 = ElectricCar("Tesla", "Model 3", 2023, 75)
    print(f"Created: {car2.get_info()}")
    print(f"Range: {car2.get_range()} miles")
    print(car2.charge())
    print()

    # Show total cars
    print(f"Total cars created: {Car.get_total_cars()}")
