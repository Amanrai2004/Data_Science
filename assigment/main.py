#Question 11:
from constants import PI, SPEED_OF_LIGHT

print(f"The value of pi is: {PI}")
print(f"The speed of light is: {SPEED_OF_LIGHT} m/s")

#Question 12:

from calculator import add, subtract, multiply, divide

# Testing the calculator functions
print(f"Addition: 5 + 3 = {add(5, 3)}")
print(f"Subtraction: 5 - 3 = {subtract(5, 3)}")
print(f"Multiplication: 5 * 3 = {multiply(5, 3)}")
print(f"Division: 5 / 3 = {divide(5, 3)}")
print(f"Division by zero: 5 / 0 = {divide(5, 0)}")




"""""
ecommerce/
│
├── ecommerce/
│   ├── __init__.py
│   ├── product_management/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   └── services.py
│   └── order_processing/
│       ├── __init__.py
│       ├── models.py
│       └── services.py
│
├── tests/
│   ├── __init__.py
│   ├── test_product_management.py
│   └── test_order_processing.py
│
├── setup.py
└── README.md
"""

