"""
Math Utilities Module
Provides basic mathematical operations
"""


def add(a, b):
    """Add two numbers"""
    return a + b


def subtract(a, b):
    """Subtract b from a"""
    return a - b


def multiply(a, b):
    """Multiply two numbers"""
    return a * b


def divide(a, b):
    """Divide a by b (with error handling)"""
    if b == 0:
        return "Error: Division by zero!"
    return a / b


def power(base, exponent):
    """Raise base to the power of exponent"""
    return base**exponent


def average(numbers):
    """Calculate average of a list of numbers"""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def is_even(number):
    """Check if a number is even"""
    return number % 2 == 0


def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# Module-level constants
PI = 3.14159265359
E = 2.71828182846

# Module metadata
__version__ = "1.0.0"
__author__ = "Python Series"


# This code runs only when module is executed directly
if __name__ == "__main__":
    print("🧮 Math Utils Module - Testing")
    print(f"add(10, 5) = {add(10, 5)}")
    print(f"subtract(10, 5) = {subtract(10, 5)}")
    print(f"multiply(4, 7) = {multiply(4, 7)}")
    print(f"divide(20, 4) = {divide(20, 4)}")
    print(f"power(2, 3) = {power(2, 3)}")
    print(f"average([1, 2, 3, 4, 5]) = {average([1, 2, 3, 4, 5])}")
    print(f"is_even(4) = {is_even(4)}")
    print(f"is_prime(7) = {is_prime(7)}")
    print(f"PI = {PI}")
