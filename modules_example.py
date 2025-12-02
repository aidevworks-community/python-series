"""
Practical Example: Using Custom Modules
This demonstrates how to import and use the modules we created
"""

# Import our custom modules
import math_utils
import string_utils
from car import Car, ElectricCar

print("=" * 80)
print("🎯 PRACTICAL EXAMPLE: USING CUSTOM MODULES")
print("=" * 80)
print()

# ============================================================================
# Using Math Utils
# ============================================================================

print("🧮 USING MATH_UTILS MODULE")
print("-" * 80)

numbers = [85, 92, 78, 90, 88]
print(f"Student scores: {numbers}")
print(f"Average score: {math_utils.average(numbers):.2f}")
print(f"Is 17 prime? {math_utils.is_prime(17)}")
print(f"Is 20 even? {math_utils.is_even(20)}")
print(f"Circle area (r=5): {math_utils.PI * math_utils.power(5, 2):.2f}")
print()

# ============================================================================
# Using String Utils
# ============================================================================

print("📝 USING STRING_UTILS MODULE")
print("-" * 80)

text = "Python Programming"
print(f"Original: '{text}'")
print(f"Reversed: '{string_utils.reverse(text)}'")
print(f"Vowel count: {string_utils.count_vowels(text)}")
print(f"Word count: {string_utils.count_words(text)}")
print(f"Snake case: '{string_utils.to_snake_case(text)}'")
print(f"Camel case: '{string_utils.to_camel_case(text)}'")

palindrome = "racecar"
print(f"Is '{palindrome}' a palindrome? {string_utils.is_palindrome(palindrome)}")
print()

# ============================================================================
# Using Car Module
# ============================================================================

print("🚗 USING CAR MODULE")
print("-" * 80)

# Create regular cars
car1 = Car("Honda", "Civic", 2020)
car2 = Car("Toyota", "Corolla", 2022)

print(f"Car 1: {car1.get_info()}")
print(car1.drive(150))
print(car1.honk())
print(f"Age: {car1.get_age()} years old")
print()

print(f"Car 2: {car2.get_info()}")
print(car2.drive(75))
print()

# Create electric car
tesla = ElectricCar("Tesla", "Model Y", 2024, 80)
print(f"Electric Car: {tesla.get_info()}")
print(f"Estimated range: {tesla.get_range()} miles")
print(tesla.charge())
print()

print(f"📊 Total cars created: {Car.get_total_cars()}")
print()

# ============================================================================
# Real-World Example: Grade Calculator
# ============================================================================

print("=" * 80)
print("🎓 REAL-WORLD EXAMPLE: STUDENT GRADE CALCULATOR")
print("=" * 80)
print()


def calculate_grade(scores):
    """Calculate letter grade based on average score"""
    avg = math_utils.average(scores)

    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"


students = {
    "Alice": [95, 88, 92, 90],
    "Bob": [78, 82, 75, 80],
    "Charlie": [88, 85, 90, 87],
}

for name, scores in students.items():
    avg = math_utils.average(scores)
    grade = calculate_grade(scores)
    print(f"{name}:")
    print(f"  Scores: {scores}")
    print(f"  Average: {avg:.2f}")
    print(f"  Grade: {grade}")
    print()

# ============================================================================
# Real-World Example: Text Analyzer
# ============================================================================

print("=" * 80)
print("📊 REAL-WORLD EXAMPLE: TEXT ANALYZER")
print("=" * 80)
print()


def analyze_text(text):
    """Analyze text using string_utils functions"""
    print(f"Original text: '{text}'")
    print(f"Character count: {len(text)}")
    print(f"Word count: {string_utils.count_words(text)}")
    print(f"Vowel count: {string_utils.count_vowels(text)}")
    print(f"Reversed: '{string_utils.reverse(text)}'")
    print(f"Capitalized: '{string_utils.capitalize_words(text)}'")
    print(f"Snake case: '{string_utils.to_snake_case(text)}'")


sample_text = "data science is awesome"
analyze_text(sample_text)
print()

# ============================================================================
# Real-World Example: Car Dealership
# ============================================================================

print("=" * 80)
print("🏪 REAL-WORLD EXAMPLE: CAR DEALERSHIP INVENTORY")
print("=" * 80)
print()

# Create inventory
inventory = [
    Car("Honda", "Accord", 2022),
    Car("Ford", "Mustang", 2021),
    ElectricCar("Tesla", "Model 3", 2023, 75),
    Car("BMW", "X5", 2023),
    ElectricCar("Nissan", "Leaf", 2022, 62),
]

print("📋 Available Cars:")
for i, car in enumerate(inventory, 1):
    print(f"  {i}. {car.get_info()}")
    if isinstance(car, ElectricCar):
        print(f"     Range: {car.get_range()} miles")

print()
print(f"Total vehicles in inventory: {len(inventory)}")
electric_count = sum(1 for car in inventory if isinstance(car, ElectricCar))
print(f"Electric vehicles: {electric_count}")
print(f"Gas vehicles: {len(inventory) - electric_count}")
print()

# ============================================================================
# Summary
# ============================================================================

print("=" * 80)
print("✅ SUMMARY")
print("=" * 80)
print(
    """
This example demonstrated:

1️⃣ Importing custom modules (math_utils, string_utils, car)
2️⃣ Using module functions in real scenarios
3️⃣ Creating reusable code organization
4️⃣ Building practical applications with modules

💡 Key Benefits:
  • Code reusability across multiple programs
  • Better organization and maintainability  
  • Easier testing and debugging
  • Collaboration-friendly structure
  • Namespace management

🚀 Next Steps:
  • Create your own utility modules
  • Organize related code into packages
  • Share modules with your team
  • Explore third-party modules (pip install)
"""
)
