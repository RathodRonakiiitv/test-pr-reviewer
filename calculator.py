"""
Simple Calculator Module
"""

def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract b from a"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide a by b"""
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

def power(base, exponent):
    """Calculate base raised to the power of exponent"""
    # This implementation has a potential issue with negative exponents
    result = 1
    for i in range(exponent):
        result *= base
    return result

def square_root(n):
    """Calculate square root using Newton's method"""
    if n < 0:
        return -1  # Bug: Should raise an exception instead of returning -1
    guess = n / 2
    for _ in range(10):
        guess = (guess + n / guess) / 2
    return guess

if __name__ == "__main__":
    print("Calculator Demo")
    print(f"5 + 3 = {add(5, 3)}")
    print(f"10 - 4 = {subtract(10, 4)}")
    print(f"6 * 7 = {multiply(6, 7)}")
    print(f"20 / 5 = {divide(20, 5)}")
    print(f"2 ^ 8 = {power(2, 8)}")
    print(f"sqrt(16) = {square_root(16)}")
