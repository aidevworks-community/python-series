## Functions in Python


def greet(name, greeting="Hello"):
    print(greeting, name)


# # greet("Alice", "Hi")  # Hi Alice


# # #######################################
def greet():
    print("Hello, Python learner!")


greet()


# # #######################3


# # #################
# # ## 🔢 MULTIPLE RETURN VALUES - Returning Multiple Results


def calculate(a, b):
    """
    This function performs two operations and returns BOTH results at once!

    a + b  → Addition operator (adds two numbers)
    a * b  → Multiplication operator (multiplies two numbers)

    Returns a tuple: (sum, product)
    """
    return a + b, a * b  # Returns tuple: (5, 6) when a=2, b=3


# # # Example 1: Unpacking both values
sum_, mul_ = calculate(2, 3)


print("=" * 60)
print("📦 Example 1: Unpacking Multiple Return Values")
print("=" * 60)
print(f"Input: a = 2, b = 3")
print(f"Sum (a + b): {sum_}")  # 2 + 3 = 5
print(f"Product (a * b): {mul_}")  # 2 * 3 = 6
print(f"Explanation:")
print(f"  → a + b = 2 + 3 = {sum_}")
print(f"  → a * b = 2 × 3 = {mul_}")
print()

# # # Example 2: Getting the tuple directly
result_tuple = calculate(4, 5)
print("📦 Example 2: Tuple Return")
print(f"Result as tuple: {result_tuple}")  # (9, 20)
print(f"  → First value (sum): {result_tuple[0]}")
print(f"  → Second value (product): {result_tuple[1]}")
print()

# # # Example 3: More examples with different numbers
print("=" * 60)
print("🧮 MORE EXAMPLES - Understanding a + b and a * b")
print("=" * 60)

# # # Test case 1
s1, p1 = calculate(10, 5)
print(f"calculate(10, 5):")
print(f"  10 + 5 = {s1}  (addition)")
print(f"  10 × 5 = {p1}  (multiplication)")
print()

# # # Test case 2
s2, p2 = calculate(7, 8)
print(f"calculate(7, 8):")
print(f"  7 + 8 = {s2}  (addition)")
print(f"  7 × 8 = {p2}  (multiplication)")
print()

# # # Test case 3: Works with floats too!
s3, p3 = calculate(2.5, 4)
print(f"calculate(2.5, 4):")
print(f"  2.5 + 4 = {s3}  (addition)")
print(f"  2.5 × 4 = {p3}  (multiplication)")
print()

# # # Test case 4: Negative numbers
s4, p4 = calculate(-3, 5)
print(f"calculate(-3, 5):")
print(f"  -3 + 5 = {s4}  (addition)")
print(f"  -3 × 5 = {p4}  (multiplication)")
print()

print("=" * 60)
print("💡 KEY CONCEPTS")
print("=" * 60)
print("✅ a + b  → Addition operator")
print("   - Adds two numbers together")
print("   - Example: 2 + 3 = 5")
print()
print("✅ a * b  → Multiplication operator")
print("   - Multiplies two numbers")
print("   - Example: 2 * 3 = 6")
print()
print("✅ Multiple Returns:")
print("   - Python can return multiple values as a tuple")
print("   - 'return a + b, a * b' returns (sum, product)")
print("   - Unpack with: sum_, mul_ = calculate(2, 3)")
print()
print("✅ Why use underscore suffix (sum_, mul_)?")
print("   - 'sum' is a built-in Python function")
print("   - Using 'sum_' avoids overwriting the built-in")
print("   - Good practice for variable naming!")
print("=" * 60)

# # #################################################


def welcome(name="Guest"):
    print("Welcome", name)


welcome()  # Welcome Guest
welcome("Nishith")  # Welcome Nishith


square = lambda x: x * x
print(square(5))  # 25
