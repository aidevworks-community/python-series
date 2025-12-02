"""
📦 PYTHON PACKAGE EXAMPLE
Demonstrates how to create and use a Python package with subpackages
"""

print("=" * 90)
print("📦 PYTHON PACKAGE TUTORIAL - COMPLETE EXAMPLE")
print("=" * 90)
print()

# ============================================================================
# PACKAGE STRUCTURE
# ============================================================================

print("=" * 90)
print("📁 PACKAGE STRUCTURE")
print("=" * 90)
print(
    """
mypackage/                      ← Main package folder
│
├── __init__.py                 ← Makes it a package (required!)
│
├── utils/                      ← Subpackage for utilities
│   ├── __init__.py            ← Makes utils a subpackage
│   ├── calculator.py          ← Arithmetic operations
│   └── formatter.py           ← Formatting utilities
│
└── models/                     ← Subpackage for data models
    ├── __init__.py            ← Makes models a subpackage
    ├── person.py              ← Person class
    └── product.py             ← Product class

Key Points:
  • Each folder needs __init__.py to be a package/subpackage
  • __init__.py can be empty or contain initialization code
  • Packages organize related modules together
  • Enables dot notation: mypackage.utils.calculator
"""
)
print()

# ============================================================================
# METHOD 1: Import entire package
# ============================================================================

print("=" * 90)
print("1️⃣ METHOD 1: Import Entire Package")
print("=" * 90)
print()

import mypackage

print("import mypackage")
print(f"✅ Package version: {mypackage.__version__}")
print()

# Access through package namespace
result = mypackage.add(15, 7)
print(f"mypackage.add(15, 7) = {result}")

formatted = mypackage.format_currency(1234.56)
print(f"mypackage.format_currency(1234.56) = {formatted}")
print()

# ============================================================================
# METHOD 2: Import specific submodules
# ============================================================================

print("=" * 90)
print("2️⃣ METHOD 2: Import Specific Submodules")
print("=" * 90)
print()

from mypackage.utils import calculator, formatter
from mypackage.models import Person, Product

print("from mypackage.utils import calculator, formatter")
print("from mypackage.models import Person, Product")
print()

# Use calculator functions
print(f"calculator.multiply(8, 9) = {calculator.multiply(8, 9)}")
print(f"calculator.power(2, 5) = {calculator.power(2, 5)}")
print(f"calculator.factorial(5) = {calculator.factorial(5)}")
print()

# Use formatter functions
print(f"formatter.format_currency(5678.90) = {formatter.format_currency(5678.90)}")
print(f"formatter.format_percentage(87.5) = {formatter.format_percentage(87.5)}")
print(f"formatter.format_phone('5551234567') = {formatter.format_phone('5551234567')}")
print()

# ============================================================================
# METHOD 3: Import specific functions/classes
# ============================================================================

print("=" * 90)
print("3️⃣ METHOD 3: Import Specific Functions/Classes")
print("=" * 90)
print()

from mypackage.utils.calculator import add, subtract, percentage
from mypackage.utils.formatter import format_date, format_file_size, format_currency
from mypackage.models.person import Person
from mypackage.models.product import Product

print("from mypackage.utils.calculator import add, subtract, percentage")
print(
    "from mypackage.utils.formatter import format_date, format_file_size, format_currency"
)
print()

# Direct function calls (no module prefix needed)
print(f"add(100, 50) = {add(100, 50)}")
print(f"subtract(100, 50) = {subtract(100, 50)}")
print(f"percentage(45, 60) = {percentage(45, 60):.2f}%")
print()

print(f"format_date() = {format_date()}")
print(f"format_file_size(2048576) = {format_file_size(2048576)}")
print()

# ============================================================================
# USING THE PERSON CLASS
# ============================================================================

print("=" * 90)
print("👤 USING THE PERSON CLASS")
print("=" * 90)
print()

# Create persons
person1 = Person("Alice", "Johnson", 28, "alice@example.com")
person2 = Person("Bob", "Smith", 35, "bob@example.com")
person3 = Person("Charlie", "Brown", 17)

print("Created 3 persons:")
print(f"1. {person1.get_full_name()} - Age: {person1.age}")
print(f"2. {person2.get_full_name()} - Age: {person2.age}")
print(f"3. {person3.get_full_name()} - Age: {person3.age}")
print()

print(f"{person1.first_name}'s initials: {person1.get_initials()}")
print(f"Is {person3.first_name} an adult? {person3.is_adult()}")
print()

print(person1.birthday())
print()

print("📊 Person Details:")
print(person2.get_info())
print()

print(f"Total persons created: {Person.get_total_persons()}")
print()

# ============================================================================
# USING THE PRODUCT CLASS
# ============================================================================

print("=" * 90)
print("🛍️ USING THE PRODUCT CLASS")
print("=" * 90)
print()

# Create products
laptop = Product("Dell XPS 15", 1299.99, 25, "Electronics")
phone = Product("iPhone 15", 999.00, 50, "Electronics")
book = Product("Python Guide", 39.99, 100, "Books")

print("📦 Product Inventory:")
print(f"1. {laptop}")
print(f"2. {phone}")
print(f"3. {book}")
print()

print("💼 Laptop Details:")
print(laptop.get_info())
print()

# Stock operations
print("📈 Stock Management:")
print(laptop.add_stock(10))
print(phone.remove_stock(5))
print()

# Apply discount
print("💰 Applying 15% discount to book:")
print(book.apply_discount(15))
print(f"New book info: {book}")
print()

# Bulk discount calculation
print("🏪 Bulk Purchase Discounts:")
original_price = 999.00
for qty in [5, 15, 60, 150]:
    bulk_price = Product.calculate_bulk_discount(original_price, qty)
    discount = ((original_price - bulk_price) / original_price) * 100
    print(f"  {qty} units: ${bulk_price:.2f} each ({discount:.0f}% off)")
print()

# ============================================================================
# REAL-WORLD EXAMPLE: E-COMMERCE SYSTEM
# ============================================================================

print("=" * 90)
print("🛒 REAL-WORLD EXAMPLE: SIMPLE E-COMMERCE SYSTEM")
print("=" * 90)
print()


class ShoppingCart:
    """Shopping cart using our package"""

    def __init__(self, customer):
        self.customer = customer
        self.items = []

    def add_item(self, product, quantity=1):
        """Add product to cart"""
        if not product.is_in_stock():
            return f"❌ {product.name} is out of stock!"

        if quantity > product.quantity:
            return f"❌ Only {product.quantity} units available!"

        self.items.append(
            {"product": product, "quantity": quantity, "price": product.price}
        )
        return f"✅ Added {quantity}x {product.name} to cart"

    def get_subtotal(self):
        """Calculate subtotal"""
        return sum(item["price"] * item["quantity"] for item in self.items)

    def get_tax(self):
        """Calculate tax"""
        return self.get_subtotal() * Product.tax_rate

    def get_total(self):
        """Calculate total with tax"""
        return self.get_subtotal() + self.get_tax()

    def show_cart(self):
        """Display cart contents"""
        print(f"🛒 Shopping Cart for {self.customer.get_full_name()}")
        print("-" * 90)

        if not self.items:
            print("Cart is empty")
            return

        for i, item in enumerate(self.items, 1):
            product = item["product"]
            qty = item["quantity"]
            price = item["price"]
            total = price * qty
            print(f"{i}. {product.name}")
            print(f"   {qty} × {format_currency(price)} = {format_currency(total)}")

        print("-" * 90)
        print(f"Subtotal: {format_currency(self.get_subtotal())}")
        print(
            f"Tax ({percentage(Product.tax_rate * 100, 100):.0f}%): {format_currency(self.get_tax())}"
        )
        print(f"TOTAL: {format_currency(self.get_total())}")


# Create customer
customer = Person("Sarah", "Wilson", 32, "sarah@example.com")

# Create products
products = [
    Product("Wireless Mouse", 29.99, 100, "Electronics"),
    Product("USB-C Cable", 15.99, 200, "Accessories"),
    Product("Laptop Bag", 49.99, 50, "Accessories"),
]

# Create shopping cart
cart = ShoppingCart(customer)

print("🛍️ Customer Shopping:")
print(cart.add_item(products[0], 2))  # 2 mice
print(cart.add_item(products[1], 3))  # 3 cables
print(cart.add_item(products[2], 1))  # 1 bag
print()

# Show cart
cart.show_cart()
print()

# ============================================================================
# SUMMARY
# ============================================================================

print("=" * 90)
print("📚 PACKAGE TUTORIAL SUMMARY")
print("=" * 90)
print(
    """
✅ What You Learned:

1️⃣ PACKAGE STRUCTURE
   • Folder with __init__.py = Package
   • Nested folders = Subpackages
   • Organize related modules together

2️⃣ IMPORT METHODS
   • import mypackage
   • from mypackage import module
   • from mypackage.module import function

3️⃣ __init__.py FILE
   • Makes folder a package
   • Can import/expose items for easier access
   • Can contain package metadata

4️⃣ BENEFITS
   • Better code organization
   • Namespace management
   • Easier maintenance
   • Reusable across projects
   • Clear project structure

5️⃣ BEST PRACTICES
   • Use descriptive package names
   • Keep subpackages focused
   • Document in __init__.py
   • Include version info
   • Use __all__ for explicit exports

🚀 NEXT STEPS:
   • Create your own package structure
   • Organize existing code into packages
   • Share packages with pip (setup.py, pyproject.toml)
   • Explore popular packages on PyPI

📦 Package Created: mypackage/
   └── utils/ (calculator, formatter)
   └── models/ (Person, Product)
"""
)
