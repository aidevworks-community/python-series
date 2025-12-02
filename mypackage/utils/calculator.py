"""
Calculator module
Provides basic arithmetic operations
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
    """Divide a by b with error handling"""
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b


def power(base, exponent):
    """Raise base to the power of exponent"""
    return base**exponent


def percentage(part, whole):
    """Calculate percentage"""
    if whole == 0:
        return 0
    return (part / whole) * 100


def factorial(n):
    """Calculate factorial of n"""
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    print("Calculator Module Test")
    print(f"add(10, 5) = {add(10, 5)}")
    print(f"subtract(10, 5) = {subtract(10, 5)}")
    print(f"multiply(4, 7) = {multiply(4, 7)}")
    print(f"divide(20, 4) = {divide(20, 4)}")
    print(f"power(2, 3) = {power(2, 3)}")
    print(f"percentage(25, 100) = {percentage(25, 100)}%")
    print(f"factorial(5) = {factorial(5)}")
