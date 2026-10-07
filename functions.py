# Python Functions


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"

    return a / b


print("Addition:", add(10, 5))

print("Subtraction:", subtract(10, 5))

print("Multiplication:", multiply(10, 5))

print("Division:", divide(10, 5))


# Function with default argument

def greet(name="User"):
    return f"Hello, {name}!"


print(greet())

print(greet("Ashwin"))