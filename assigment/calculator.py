# calculator.py
"""12. Write a Python module named calculator.py containing functions for addition, subtraction,
multiplication, and division."""

def add(a, b):
    """
    Return the sum of two numbers.
    """
    return a + b

def subtract(a, b):
    """
    Return the difference between two numbers.
    """
    return a - b

def multiply(a, b):
    """
    Return the product of two numbers.
    """
    return a * b

def divide(a, b):
    """
    Return the quotient of two numbers.
    If the divisor is zero, return 'Undefined' as division by zero is not allowed.
    """
    if b == 0:
        return 'Undefined'
    else:
        return a / b
