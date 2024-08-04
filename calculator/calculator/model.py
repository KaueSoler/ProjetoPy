import math

class CalculatorModel:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def power(self, base, exponent):
        return math.pow(base, exponent)

    def sqrt(self, value):
        if value < 0:
            raise ValueError("Cannot compute square root of negative number")
        return math.sqrt(value)

    # Add more operations as needed
