# https://github.com/JosiahCaballero/-lab10--J.C---M.L-
# Partner 1: Maria Luiza C Nogueira
# Partner 2: Josiah Caballero
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

def log(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Logarithm base must be > 0 and ≠ 1, and argument must be > 0.")
    return math.log(b, a)

def exp(a, b):
    return a ** b

def square_root(a):
    try:
        if a < 0:
            raise ValueError("Cannot take square root of a negative number.")
        return math.sqrt(a)
    except ValueError as e:
        return str(e)


def hypotenuse(a, b):
    try:
        return math.hypot(a, b)
    except Exception as e:
        return str(e)





