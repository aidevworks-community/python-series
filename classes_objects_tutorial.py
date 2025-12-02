"""
📦 PYTHON CLASSES & OBJECTS - COMPLETE TUTORIAL
Object-Oriented Programming (OOP) in Python
"""

print("=" * 90)
print("🎯 PYTHON CLASSES & OBJECTS - COMPLETE TUTORIAL")
print("=" * 90)
print()

# ============================================================================
# 1. WHAT ARE CLASSES AND OBJECTS?
# ============================================================================

print("=" * 90)
print("1️⃣ WHAT ARE CLASSES AND OBJECTS?")
print("=" * 90)
print(
    """
🏗️ CLASS = Blueprint/Template
   • Defines properties (attributes) and behaviors (methods)
   • Like a cookie cutter or architectural blueprint
   
🍪 OBJECT = Instance of a Class
   • Actual thing created from the blueprint
   • Each object has its own data

Example:
   Class: Dog (blueprint)
   Objects: my_dog, your_dog (actual dogs with specific names, ages, etc.)
"""
)
print()

# ============================================================================
# 2. CREATING A SIMPLE CLASS
# ============================================================================

print("=" * 90)
print("2️⃣ CREATING A SIMPLE CLASS")
print("=" * 90)
print()


class Dog:
    """A simple Dog class"""

    def __init__(self, name, age):
        """Initialize dog attributes"""
        self.name = name  # Instance variable
        self.age = age

    def bark(self):
        """Make the dog bark"""
        return f"{self.name} says Woof! 🐕"

    def get_info(self):
        """Return dog information"""
        return f"{self.name} is {self.age} years old"


# Creating objects (instances)
print("Creating Dog objects:")
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

print(f"Dog 1: {dog1.get_info()}")
print(f"Dog 2: {dog2.get_info()}")
print(dog1.bark())
print(dog2.bark())
print()

print("🔑 Key Concepts:")
print("  • __init__() = Constructor (runs when object is created)")
print("  • self = Reference to the current instance")
print("  • self.name = Instance variable (unique to each object)")
print("  • bark() = Instance method (function inside a class)")
print()

# ============================================================================
# 3. CLASS vs INSTANCE VARIABLES
# ============================================================================

print("=" * 90)
print("3️⃣ CLASS vs INSTANCE VARIABLES")
print("=" * 90)
print()


class Employee:
    """Employee class demonstrating class and instance variables"""

    # Class variable (shared by ALL instances)
    company_name = "TechCorp"
    employee_count = 0

    def __init__(self, name, position, salary):
        """Initialize instance variables"""
        # Instance variables (unique to each object)
        self.name = name
        self.position = position
        self.salary = salary
        Employee.employee_count += 1

    def get_details(self):
        """Return employee details"""
        return f"{self.name} - {self.position} at {Employee.company_name}"

    def give_raise(self, amount):
        """Increase salary"""
        self.salary += amount
        return f"{self.name}'s new salary: ${self.salary:,.2f}"


# Create employees
emp1 = Employee("Alice Johnson", "Software Engineer", 85000)
emp2 = Employee("Bob Smith", "Data Scientist", 90000)
emp3 = Employee("Carol Davis", "Product Manager", 95000)

print("📊 Employee Details:")
print(emp1.get_details())
print(emp2.get_details())
print(emp3.get_details())
print()

print(f"💼 Company: {Employee.company_name}")
print(f"👥 Total Employees: {Employee.employee_count}")
print()

print(emp1.give_raise(5000))
print()

print("🔑 Key Difference:")
print("  • Class Variable (company_name): Shared by ALL employees")
print("  • Instance Variable (name, salary): Unique to each employee")
print()

# ============================================================================
# 4. METHODS: Instance, Class, and Static
# ============================================================================

print("=" * 90)
print("4️⃣ TYPES OF METHODS")
print("=" * 90)
print()


class BankAccount:
    """Bank account with different method types"""

    # Class variable
    interest_rate = 0.03  # 3%
    total_accounts = 0

    def __init__(self, owner, balance=0):
        """Initialize account"""
        self.owner = owner
        self.balance = balance
        self.transactions = []
        BankAccount.total_accounts += 1

    # Instance method (operates on instance data)
    def deposit(self, amount):
        """Deposit money"""
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposit: +${amount:.2f}")
            return f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}"
        return "Invalid amount"

    def withdraw(self, amount):
        """Withdraw money"""
        if amount > self.balance:
            return "Insufficient funds!"
        if amount > 0:
            self.balance -= amount
            self.transactions.append(f"Withdrawal: -${amount:.2f}")
            return f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}"
        return "Invalid amount"

    def get_balance(self):
        """Get current balance"""
        return f"{self.owner}'s balance: ${self.balance:.2f}"

    # Class method (operates on class data)
    @classmethod
    def set_interest_rate(cls, new_rate):
        """Change interest rate for all accounts"""
        cls.interest_rate = new_rate
        return f"Interest rate updated to {new_rate * 100}%"

    @classmethod
    def get_total_accounts(cls):
        """Get total number of accounts"""
        return cls.total_accounts

    # Static method (doesn't use instance or class data)
    @staticmethod
    def is_valid_amount(amount):
        """Check if amount is valid"""
        return amount > 0 and amount < 1000000


# Using the BankAccount class
print("🏦 Bank Account Operations:")
account1 = BankAccount("John Doe", 1000)
account2 = BankAccount("Jane Smith", 500)

print(account1.get_balance())
print(account1.deposit(500))
print(account1.withdraw(200))
print()

print(account2.get_balance())
print(account2.deposit(1000))
print()

# Using class method
print(BankAccount.set_interest_rate(0.04))
print(f"Total accounts created: {BankAccount.get_total_accounts()}")
print()

# Using static method
print(f"Is $500 valid? {BankAccount.is_valid_amount(500)}")
print(f"Is $2,000,000 valid? {BankAccount.is_valid_amount(2000000)}")
print()

print("🔑 Method Types:")
print("  • Instance Method: Uses self, accesses instance data")
print("  • Class Method (@classmethod): Uses cls, accesses class data")
print("  • Static Method (@staticmethod): Independent utility function")
print()

# ============================================================================
# 5. INHERITANCE
# ============================================================================

print("=" * 90)
print("5️⃣ INHERITANCE - Creating Child Classes")
print("=" * 90)
print()


class Vehicle:
    """Parent class - Vehicle"""

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def get_info(self):
        """Return vehicle info"""
        return f"{self.year} {self.brand} {self.model}"

    def start(self):
        """Start the vehicle"""
        return f"{self.brand} {self.model} is starting..."


class Car(Vehicle):
    """Child class - Car inherits from Vehicle"""

    def __init__(self, brand, model, year, num_doors):
        super().__init__(brand, model, year)  # Call parent constructor
        self.num_doors = num_doors

    def honk(self):
        """Car-specific method"""
        return f"{self.brand} goes beep beep! 🚗"


class Motorcycle(Vehicle):
    """Child class - Motorcycle inherits from Vehicle"""

    def __init__(self, brand, model, year, engine_cc):
        super().__init__(brand, model, year)
        self.engine_cc = engine_cc

    def rev_engine(self):
        """Motorcycle-specific method"""
        return f"{self.brand} revs {self.engine_cc}cc engine! 🏍️"


# Using inheritance
print("🚗 Creating Vehicles:")
car = Car("Toyota", "Camry", 2023, 4)
bike = Motorcycle("Harley-Davidson", "Street 750", 2022, 750)

print(car.get_info())  # Inherited method
print(car.start())  # Inherited method
print(car.honk())  # Car-specific method
print()

print(bike.get_info())  # Inherited method
print(bike.start())  # Inherited method
print(bike.rev_engine())  # Bike-specific method
print()

print("🔑 Inheritance Benefits:")
print("  • Code reuse (DRY - Don't Repeat Yourself)")
print("  • Child classes inherit parent methods and attributes")
print("  • super() calls parent class constructor")
print("  • Child can add new methods and override parent methods")
print()

# ============================================================================
# 6. ENCAPSULATION (Private/Public)
# ============================================================================

print("=" * 90)
print("6️⃣ ENCAPSULATION - Public, Protected, Private")
print("=" * 90)
print()


class Student:
    """Student class demonstrating encapsulation"""

    def __init__(self, name, student_id, gpa):
        self.name = name  # Public
        self._student_id = student_id  # Protected (convention: single _)
        self.__gpa = gpa  # Private (name mangling: double __)

    # Getter method (to access private attribute)
    def get_gpa(self):
        """Get student's GPA"""
        return self.__gpa

    # Setter method (to modify private attribute with validation)
    def set_gpa(self, new_gpa):
        """Set student's GPA with validation"""
        if 0.0 <= new_gpa <= 4.0:
            self.__gpa = new_gpa
            return f"GPA updated to {new_gpa}"
        return "Invalid GPA! Must be between 0.0 and 4.0"

    def get_info(self):
        """Return student information"""
        return f"Student: {self.name} (ID: {self._student_id}, GPA: {self.__gpa})"


# Using encapsulation
print("👨‍🎓 Student Example:")
student = Student("Mike Wilson", "S12345", 3.8)

print(f"Name (public): {student.name}")
print(f"Student ID (protected): {student._student_id}")
# print(student.__gpa)  # ❌ This would cause an error!

# Access private attribute through getter
print(f"GPA (private, via getter): {student.get_gpa()}")

# Modify private attribute through setter
print(student.set_gpa(3.9))
print(student.set_gpa(5.0))  # Invalid!
print()

print("🔑 Access Levels:")
print("  • public (no prefix): Accessible everywhere")
print("  • _protected (single _): Internal use (convention only)")
print("  • __private (double __): Not directly accessible outside class")
print("  • Use getters/setters for controlled access")
print()

# ============================================================================
# 7. SPECIAL (MAGIC) METHODS
# ============================================================================

print("=" * 90)
print("7️⃣ SPECIAL METHODS (__magic__ methods)")
print("=" * 90)
print()


class Book:
    """Book class with special methods"""

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        """String representation (for users)"""
        return f"'{self.title}' by {self.author}"

    def __repr__(self):
        """Developer representation"""
        return f"Book('{self.title}', '{self.author}', {self.pages})"

    def __len__(self):
        """Return length (number of pages)"""
        return self.pages

    def __eq__(self, other):
        """Check equality"""
        return self.title == other.title and self.author == other.author

    def __lt__(self, other):
        """Less than comparison (by pages)"""
        return self.pages < other.pages


# Using special methods
print("📚 Book Examples:")
book1 = Book("Python Basics", "John Smith", 250)
book2 = Book("Advanced Python", "Jane Doe", 450)
book3 = Book("Python Basics", "John Smith", 250)

print(f"Book 1: {book1}")  # Uses __str__
print(f"Book 2: {book2}")
print(f"Repr: {repr(book1)}")  # Uses __repr__
print()

print(f"Length of book1: {len(book1)} pages")  # Uses __len__
print()

print(f"book1 == book2? {book1 == book2}")  # Uses __eq__
print(f"book1 == book3? {book1 == book3}")
print()

print(f"book1 < book2? {book1 < book2}")  # Uses __lt__
print()

print("🔑 Common Special Methods:")
print("  • __init__: Constructor")
print("  • __str__: User-friendly string")
print("  • __repr__: Developer-friendly representation")
print("  • __len__: Length")
print("  • __eq__: Equality (==)")
print("  • __lt__, __gt__: Comparisons (<, >)")
print("  • __add__, __sub__: Math operations (+, -)")
print()

# ============================================================================
# 8. REAL-WORLD EXAMPLE: E-COMMERCE SYSTEM
# ============================================================================

print("=" * 90)
print("8️⃣ REAL-WORLD EXAMPLE: E-COMMERCE SYSTEM")
print("=" * 90)
print()


class Product:
    """Product in an online store"""

    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def is_available(self, quantity=1):
        """Check if product is available"""
        return self.stock >= quantity

    def reduce_stock(self, quantity):
        """Reduce stock after purchase"""
        if self.is_available(quantity):
            self.stock -= quantity
            return True
        return False

    def __str__(self):
        return f"{self.name} - ${self.price:.2f} ({self.stock} in stock)"


class Customer:
    """Customer with shopping cart"""

    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.cart = []

    def add_to_cart(self, product, quantity=1):
        """Add product to cart"""
        if product.is_available(quantity):
            self.cart.append({"product": product, "quantity": quantity})
            return f"✅ Added {quantity}x {product.name} to cart"
        return f"❌ Only {product.stock} {product.name} available"

    def view_cart(self):
        """View shopping cart"""
        if not self.cart:
            return "Cart is empty"

        result = f"🛒 {self.name}'s Shopping Cart:\n"
        total = 0
        for i, item in enumerate(self.cart, 1):
            product = item["product"]
            qty = item["quantity"]
            subtotal = product.price * qty
            total += subtotal
            result += f"  {i}. {product.name} x{qty} = ${subtotal:.2f}\n"
        result += f"  Total: ${total:.2f}"
        return result

    def checkout(self):
        """Process checkout"""
        if not self.cart:
            return "Cart is empty!"

        total = 0
        for item in self.cart:
            product = item["product"]
            qty = item["quantity"]
            if product.reduce_stock(qty):
                total += product.price * qty
            else:
                return f"❌ Checkout failed: {product.name} out of stock"

        self.cart = []
        return f"✅ Checkout successful! Total: ${total:.2f}"


# Using the e-commerce system
print("🛍️ E-Commerce System Demo:")
print()

# Create products
laptop = Product("P001", "Laptop", 999.99, 10)
mouse = Product("P002", "Wireless Mouse", 29.99, 50)
keyboard = Product("P003", "Mechanical Keyboard", 79.99, 25)

print("📦 Available Products:")
print(f"1. {laptop}")
print(f"2. {mouse}")
print(f"3. {keyboard}")
print()

# Create customer
customer = Customer("C001", "Sarah Johnson", "sarah@example.com")

# Shopping
print("🛒 Shopping:")
print(customer.add_to_cart(laptop, 1))
print(customer.add_to_cart(mouse, 2))
print(customer.add_to_cart(keyboard, 1))
print()

# View cart
print(customer.view_cart())
print()

# Checkout
print("💳 Checkout:")
print(customer.checkout())
print()

# Check updated stock
print("📦 Updated Stock:")
print(f"1. {laptop}")
print(f"2. {mouse}")
print(f"3. {keyboard}")
print()

# ============================================================================
# 9. INTERFACES (Abstract Base Classes)
# ============================================================================

print("=" * 90)
print("9️⃣ INTERFACES - Abstract Base Classes (ABC)")
print("=" * 90)
print()

from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    """Abstract base class (Interface) for payment methods"""

    @abstractmethod
    def process_payment(self, amount):
        """All payment methods must implement this"""
        pass

    @abstractmethod
    def validate(self):
        """All payment methods must validate"""
        pass

    def get_receipt(self, amount):
        """Concrete method (optional to override)"""
        return f"Receipt: ${amount:.2f} processed"


class CreditCard(PaymentMethod):
    """Credit card payment implementation"""

    def __init__(self, card_number, cvv, expiry):
        self.card_number = card_number
        self.cvv = cvv
        self.expiry = expiry

    def process_payment(self, amount):
        """Implement abstract method"""
        if self.validate():
            return f"✅ ${amount:.2f} charged to card ****{self.card_number[-4:]}"
        return "❌ Payment failed: Invalid card"

    def validate(self):
        """Implement abstract method"""
        # Simple validation
        return len(self.card_number) == 16 and len(self.cvv) == 3


class PayPal(PaymentMethod):
    """PayPal payment implementation"""

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def process_payment(self, amount):
        """Implement abstract method"""
        if self.validate():
            return f"✅ ${amount:.2f} paid via PayPal ({self.email})"
        return "❌ Payment failed: Invalid PayPal account"

    def validate(self):
        """Implement abstract method"""
        return "@" in self.email and len(self.password) > 0


class Cryptocurrency(PaymentMethod):
    """Cryptocurrency payment implementation"""

    def __init__(self, wallet_address, coin_type="Bitcoin"):
        self.wallet_address = wallet_address
        self.coin_type = coin_type

    def process_payment(self, amount):
        """Implement abstract method"""
        if self.validate():
            return f"✅ ${amount:.2f} paid via {self.coin_type} (wallet: {self.wallet_address[:8]}...)"
        return "❌ Payment failed: Invalid wallet"

    def validate(self):
        """Implement abstract method"""
        return len(self.wallet_address) >= 26


# Function that works with any PaymentMethod (Polymorphism)
def process_order(payment_method, amount):
    """Process order with any payment method"""
    print(f"Processing ${amount:.2f} payment...")
    result = payment_method.process_payment(amount)
    print(result)
    if "✅" in result:
        print(payment_method.get_receipt(amount))


# Using interfaces
print("💳 Payment Methods Example:")
print()

# Create different payment methods
credit_card = CreditCard("1234567812345678", "123", "12/25")
paypal = PayPal("user@example.com", "secure_password")
crypto = Cryptocurrency("1A2B3C4D5E6F7G8H9I0J1K2L3M4N5O6P")

# Process payments with different methods
print("1. Credit Card Payment:")
process_order(credit_card, 99.99)
print()

print("2. PayPal Payment:")
process_order(paypal, 149.50)
print()

print("3. Cryptocurrency Payment:")
process_order(crypto, 299.99)
print()

print("🔑 Interface Key Points:")
print("  • ABC = Abstract Base Class (interface)")
print("  • @abstractmethod = Must be implemented by child classes")
print("  • Can't instantiate abstract class directly")
print("  • Ensures all implementations have required methods")
print("  • Enables polymorphism (use any implementation interchangeably)")
print()

# Demonstrate that you can't instantiate ABC
print("⚠️ Cannot create instance of abstract class:")
try:
    invalid = PaymentMethod()
except TypeError as e:
    print(f"   Error: {e}")
print()

# ============================================================================
# 10. POLYMORPHISM WITH INTERFACES
# ============================================================================

print("=" * 90)
print("🔟 POLYMORPHISM - Multiple Forms, Same Interface")
print("=" * 90)
print()


class Shape(ABC):
    """Abstract shape interface"""

    @abstractmethod
    def area(self):
        """Calculate area"""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate perimeter"""
        pass

    def describe(self):
        """Describe the shape"""
        return f"{self.__class__.__name__}: Area={self.area():.2f}, Perimeter={self.perimeter():.2f}"


class Rectangle(Shape):
    """Rectangle implementation"""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Circle(Shape):
    """Circle implementation"""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius**2

    def perimeter(self):
        return 2 * 3.14159 * self.radius


class Triangle(Shape):
    """Triangle implementation"""

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        # Heron's formula
        s = (self.a + self.b + self.c) / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5

    def perimeter(self):
        return self.a + self.b + self.c


# Polymorphism in action
print("📐 Shapes Example (Polymorphism):")
print()

shapes = [Rectangle(5, 10), Circle(7), Triangle(3, 4, 5)]

# Same interface, different implementations
for shape in shapes:
    print(f"  {shape.describe()}")

print()


# Calculate total area (works with any shape!)
def calculate_total_area(shape_list):
    """Calculate total area of all shapes"""
    return sum(shape.area() for shape in shape_list)


total = calculate_total_area(shapes)
print(f"📊 Total area of all shapes: {total:.2f}")
print()

print("🔑 Polymorphism Benefits:")
print("  • Write code that works with any implementation")
print("  • Same interface, different behavior")
print("  • Easy to add new types without changing existing code")
print("  • 'Duck typing': If it has area() and perimeter(), it's a Shape!")
print()

# ============================================================================
# SUMMARY
# ============================================================================

print("=" * 90)
print("📚 CLASSES & OBJECTS SUMMARY")
print("=" * 90)
print(
    """
✅ KEY CONCEPTS COVERED:

1️⃣ CLASS & OBJECT
   • Class = Blueprint
   • Object = Instance of class
   • __init__() = Constructor

2️⃣ VARIABLES
   • Instance variables (self.x)
   • Class variables (shared)

3️⃣ METHODS
   • Instance methods (self)
   • Class methods (@classmethod, cls)
   • Static methods (@staticmethod)

4️⃣ INHERITANCE
   • Parent/child relationship
   • Code reuse with super()
   • Method overriding

5️⃣ ENCAPSULATION
   • Public (no prefix)
   • Protected (_prefix)
   • Private (__prefix)

6️⃣ SPECIAL METHODS
   • __init__, __str__, __repr__
   • __len__, __eq__, __lt__

7️⃣ REAL-WORLD APPLICATION
   • Product, Customer classes
   • Shopping cart system

8️⃣ INTERFACES (ABC)
   • Abstract base classes
   • @abstractmethod decorator
   • Enforce implementation contracts

9️⃣ POLYMORPHISM
   • Multiple forms, same interface
   • Duck typing
   • Write flexible, reusable code

🎯 WHY USE OOP?
  ✓ Code organization
  ✓ Reusability (DRY)
  ✓ Maintainability
  ✓ Modeling real-world entities
  ✓ Encapsulation & data hiding
  ✓ Polymorphism & flexibility

🚀 NEXT STEPS:
  • Practice creating your own classes
  • Model real-world objects
  • Use inheritance for related classes
  • Implement interfaces with ABC
  • Explore more special methods
  • Study design patterns (Factory, Singleton, etc.)
"""
)
