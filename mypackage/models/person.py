"""
Person model
Represents a person with basic information
"""


class Person:
    """
    A class representing a person
    """

    # Class variable to track total persons
    total_persons = 0

    def __init__(self, first_name, last_name, age, email=None):
        """Initialize a Person"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        Person.total_persons += 1

    def get_full_name(self):
        """Return full name"""
        return f"{self.first_name} {self.last_name}"

    def get_initials(self):
        """Return initials"""
        return f"{self.first_name[0]}.{self.last_name[0]}."

    def is_adult(self):
        """Check if person is 18 or older"""
        return self.age >= 18

    def birthday(self):
        """Increment age by 1"""
        self.age += 1
        return f"Happy Birthday {self.first_name}! You are now {self.age} years old!"

    def update_email(self, new_email):
        """Update email address"""
        self.email = new_email

    def get_info(self):
        """Return formatted information"""
        info = f"Name: {self.get_full_name()}\nAge: {self.age}"
        if self.email:
            info += f"\nEmail: {self.email}"
        return info

    def __str__(self):
        """String representation"""
        return self.get_full_name()

    def __repr__(self):
        """Developer representation"""
        return f"Person('{self.first_name}', '{self.last_name}', {self.age})"

    @classmethod
    def get_total_persons(cls):
        """Get total number of persons created"""
        return cls.total_persons

    @staticmethod
    def is_valid_age(age):
        """Check if age is valid"""
        return 0 <= age <= 150


if __name__ == "__main__":
    print("Person Model Test")

    person1 = Person("John", "Doe", 30, "john@example.com")
    print(person1.get_info())
    print(f"Initials: {person1.get_initials()}")
    print(f"Is adult? {person1.is_adult()}")
    print(person1.birthday())
    print()

    person2 = Person("Jane", "Smith", 25)
    print(person2.get_info())
    print()

    print(f"Total persons: {Person.get_total_persons()}")
