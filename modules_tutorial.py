## 📦 PYTHON MODULES TUTORIAL
## Modules = Reusable code organized in separate files

"""
What is a Module?
- A module is a Python file (.py) containing functions, classes, and variables
- It allows you to organize code and reuse it across different programs
- Python has built-in modules (math, random) and you can create your own
"""

print("=" * 80)
print("📦 PYTHON MODULES - COMPLETE TUTORIAL")
print("=" * 80)
print()

# ============================================================================
# 1. IMPORTING BUILT-IN MODULES
# ============================================================================

print("=" * 80)
print("1️⃣ IMPORTING BUILT-IN MODULES")
print("=" * 80)
print()

# Method 1: Import entire module
import math

print("🔹 Method 1: import math")
print(f"math.sqrt(16) = {math.sqrt(16)}")
print(f"math.pi = {math.pi}")
print(f"math.pow(2, 3) = {math.pow(2, 3)}")
print()

# Method 2: Import specific functions
from math import factorial, ceil

print("🔹 Method 2: from math import factorial, ceil")
print(f"factorial(5) = {factorial(5)}")  # No need for math.
print(f"ceil(4.3) = {ceil(4.3)}")
print()

# Method 3: Import with alias
import math as m

print("🔹 Method 3: import math as m")
print(f"m.floor(4.9) = {m.floor(4.9)}")
print()

# Method 4: Import everything (not recommended)
from math import *

print("🔹 Method 4: from math import * (use sparingly!)")
print(f"sin(pi/2) = {sin(pi/2):.2f}")
print("⚠️ Can cause naming conflicts, not recommended")
print()

# ============================================================================
# 2. COMMONLY USED BUILT-IN MODULES
# ============================================================================

print("=" * 80)
print("2️⃣ COMMONLY USED BUILT-IN MODULES")
print("=" * 80)
print()

# RANDOM MODULE
import random

print("🎲 RANDOM MODULE - Random numbers and choices")
print(f"random.randint(1, 10) = {random.randint(1, 10)}")  # Random integer
print(f"random.random() = {random.random():.4f}")  # Float between 0 and 1
print(
    f"random.choice(['red', 'blue', 'green']) = {random.choice(['red', 'blue', 'green'])}"
)
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(f"random.shuffle([1,2,3,4,5]) = {numbers}")
print()

# DATETIME MODULE
from datetime import datetime, date, timedelta

print("📅 DATETIME MODULE - Date and time operations")
print(f"datetime.now() = {datetime.now()}")
print(f"date.today() = {date.today()}")
print(f"Tomorrow = {date.today() + timedelta(days=1)}")
print()

# OS MODULE
import os

print("💻 OS MODULE - Operating system operations")
print(f"os.getcwd() = {os.getcwd()}")  # Current directory
print(f"os.name = {os.name}")  # Operating system name
print(f"Home directory = {os.path.expanduser('~')}")
print()

# SYS MODULE
import sys

print("⚙️ SYS MODULE - System-specific parameters")
print(f"Python version: {sys.version.split()[0]}")
print(f"Platform: {sys.platform}")
print()

# ============================================================================
# 3. CREATING YOUR OWN MODULE
# ============================================================================

print("=" * 80)
print("3️⃣ CREATING YOUR OWN MODULES")
print("=" * 80)
print()

print("📝 To create a module:")
print("  1. Create a new .py file (e.g., calculator.py)")
print("  2. Write functions, classes, or variables")
print("  3. Import it in another file: import calculator")
print()

print("📂 Example module structure:")
print(
    """
calculator.py:
    def add(a, b):
        return a + b
    
    def subtract(a, b):
        return a - b
    
    PI = 3.14159

main.py:
    import calculator
    
    result = calculator.add(5, 3)
    print(result)  # Output: 8
"""
)
print()

# ============================================================================
# 4. IMPORTING CUSTOM MODULES (Demo)
# ============================================================================

print("=" * 80)
print("4️⃣ IMPORTING CUSTOM MODULES - LIVE DEMO")
print("=" * 80)
print()

print("🔧 Creating custom modules:")
print("  See: math_utils.py, string_utils.py, and car.py")
print("  Run this file after creating those modules!")
print()

# Try to import custom modules (if they exist)
try:
    import math_utils

    print("✅ Successfully imported math_utils")
    print(f"math_utils.add(10, 5) = {math_utils.add(10, 5)}")
    print(f"math_utils.multiply(4, 7) = {math_utils.multiply(4, 7)}")
    print()
except ImportError:
    print("⚠️ math_utils.py not found (create it to see it work!)")
    print()

try:
    import string_utils

    print("✅ Successfully imported string_utils")
    print(f"string_utils.reverse('Python') = {string_utils.reverse('Python')}")
    print(f"string_utils.count_vowels('Hello') = {string_utils.count_vowels('Hello')}")
    print()
except ImportError:
    print("⚠️ string_utils.py not found")
    print()

try:
    from car import Car

    print("✅ Successfully imported Car class")
    my_car = Car("Tesla", "Model 3", 2023)
    print(f"Created: {my_car.get_info()}")
    print()
except ImportError:
    print("⚠️ car.py not found")
    print()

# ============================================================================
# 5. MODULE ATTRIBUTES
# ============================================================================

print("=" * 80)
print("5️⃣ MODULE ATTRIBUTES")
print("=" * 80)
print()

print("🔹 __name__ attribute:")
print(f"This module's __name__ = {__name__}")
print("When you run a file directly, __name__ == '__main__'")
print("When you import a file, __name__ == 'module_name'")
print()

print("🔹 Useful for running code only when executed directly:")
print(
    """
if __name__ == '__main__':
    # This code only runs when file is executed directly
    # Not when imported as a module
    main()
"""
)
print()

# ============================================================================
# 6. PACKAGE vs MODULE
# ============================================================================

print("=" * 80)
print("6️⃣ PACKAGE VS MODULE")
print("=" * 80)
print()

print("📄 MODULE = Single .py file")
print("  Example: calculator.py")
print()

print("📦 PACKAGE = Folder containing multiple modules + __init__.py")
print(
    """
  Example structure:
  mypackage/
      __init__.py
      module1.py
      module2.py
      subpackage/
          __init__.py
          module3.py
"""
)
print()

print("📥 Importing from packages:")
print("  from mypackage import module1")
print("  from mypackage.subpackage import module3")
print()

# ============================================================================
# 7. USEFUL MODULE FUNCTIONS
# ============================================================================

print("=" * 80)
print("7️⃣ USEFUL MODULE FUNCTIONS")
print("=" * 80)
print()

print("🔹 dir() - List all attributes/functions in a module:")
print(f"dir(math)[:5] = {dir(math)[:5]}")  # First 5 items
print()

print("🔹 help() - Get documentation:")
print("help(math.sqrt)  # Shows detailed documentation")
print()


# ============================================================================
# 8. BEST PRACTICES
# ============================================================================

print("=" * 80)
print("8️⃣ MODULE BEST PRACTICES")
print("=" * 80)
print()

print("✅ DO:")
print("  • Use descriptive module names (lowercase, underscores)")
print("  • Import at the top of the file")
print("  • Use specific imports: from module import function")
print("  • Use aliases for long names: import numpy as np")
print("  • Group imports: stdlib → third-party → local")
print()

print("❌ DON'T:")
print("  • Use 'from module import *' (pollutes namespace)")
print("  • Create circular imports (module1 imports module2, vice versa)")
print("  • Use non-descriptive names (a.py, temp.py)")
print("  • Mix functionality (keep modules focused)")
print()

# ============================================================================
# SUMMARY
# ============================================================================

print("=" * 80)
print("📚 SUMMARY")
print("=" * 80)
print(
    """
🎯 KEY CONCEPTS:
  1. Modules = Reusable Python files (.py)
  2. Import with: import, from...import, or aliases (as)
  3. Built-in modules: math, random, datetime, os, sys
  4. Create custom modules by writing .py files
  5. Packages = Folders with __init__.py + multiple modules
  6. Use __name__ == '__main__' for executable code
  7. dir() and help() for exploring modules

💡 WHY USE MODULES?
  ✓ Code organization
  ✓ Reusability
  ✓ Namespace management
  ✓ Maintainability
  ✓ Collaboration

📁 NEXT STEPS:
  → Create math_utils.py, string_utils.py, car.py
  → Import and use them in your programs
  → Explore more built-in modules
  → Create your own package structure
"""
)
