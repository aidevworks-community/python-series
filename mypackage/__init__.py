"""
MyPackage - A sample Python package
Version: 1.0.0

This package demonstrates proper Python package structure
with subpackages, modules, and __init__.py files.
"""

# Package metadata
__version__ = "1.0.0"
__author__ = "Python Series"
__email__ = "contact@pythonseries.com"

# Import key functions/classes for easier access
from mypackage.utils.calculator import add, subtract, multiply, divide
from mypackage.utils.formatter import format_currency, format_date
from mypackage.models.person import Person
from mypackage.models.product import Product

# Define what gets imported with "from mypackage import *"
__all__ = [
    "add",
    "subtract",
    "multiply",
    "divide",
    "format_currency",
    "format_date",
    "Person",
    "Product",
    "__version__",
]

# Package initialization message
print(f"📦 MyPackage v{__version__} loaded successfully!")
