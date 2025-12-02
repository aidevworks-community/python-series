"""
Product model
Represents a product with price and inventory
"""


class Product:
    """
    A class representing a product
    """

    # Class variable for tax rate
    tax_rate = 0.08  # 8% tax

    def __init__(self, name, price, quantity=0, category="General"):
        """Initialize a Product"""
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category

    def get_total_value(self):
        """Calculate total inventory value"""
        return self.price * self.quantity

    def get_price_with_tax(self):
        """Calculate price including tax"""
        return self.price * (1 + Product.tax_rate)

    def add_stock(self, amount):
        """Add stock to inventory"""
        if amount < 0:
            raise ValueError("Cannot add negative stock")
        self.quantity += amount
        return f"Added {amount} units. New quantity: {self.quantity}"

    def remove_stock(self, amount):
        """Remove stock from inventory"""
        if amount < 0:
            raise ValueError("Cannot remove negative stock")
        if amount > self.quantity:
            raise ValueError(f"Not enough stock. Available: {self.quantity}")
        self.quantity -= amount
        return f"Removed {amount} units. Remaining: {self.quantity}"

    def is_in_stock(self):
        """Check if product is in stock"""
        return self.quantity > 0

    def apply_discount(self, discount_percentage):
        """Apply discount to price"""
        if not 0 <= discount_percentage <= 100:
            raise ValueError("Discount must be between 0 and 100")
        discount_amount = self.price * (discount_percentage / 100)
        self.price -= discount_amount
        return f"Discount applied! New price: ${self.price:.2f}"

    def get_info(self):
        """Return formatted product information"""
        return (
            f"Product: {self.name}\n"
            f"Category: {self.category}\n"
            f"Price: ${self.price:.2f}\n"
            f"Price (with tax): ${self.get_price_with_tax():.2f}\n"
            f"Quantity: {self.quantity}\n"
            f"Total Value: ${self.get_total_value():.2f}\n"
            f"In Stock: {'Yes' if self.is_in_stock() else 'No'}"
        )

    def __str__(self):
        """String representation"""
        return f"{self.name} - ${self.price:.2f} ({self.quantity} in stock)"

    def __repr__(self):
        """Developer representation"""
        return (
            f"Product('{self.name}', {self.price}, {self.quantity}, '{self.category}')"
        )

    @classmethod
    def set_tax_rate(cls, new_rate):
        """Update tax rate for all products"""
        cls.tax_rate = new_rate

    @staticmethod
    def calculate_bulk_discount(price, quantity):
        """Calculate bulk purchase discount"""
        if quantity >= 100:
            return price * 0.8  # 20% discount
        elif quantity >= 50:
            return price * 0.9  # 10% discount
        elif quantity >= 10:
            return price * 0.95  # 5% discount
        return price


if __name__ == "__main__":
    print("Product Model Test")

    product1 = Product("Laptop", 999.99, 50, "Electronics")
    print(product1.get_info())
    print()

    print(product1.add_stock(25))
    print(product1.remove_stock(10))
    print(product1.apply_discount(10))
    print()

    print(
        f"Bulk discount (100 units): ${Product.calculate_bulk_discount(999.99, 100):.2f}"
    )
