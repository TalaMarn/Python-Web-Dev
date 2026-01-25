# basic function example

def greet(name="Guest"):
    return f"Hello, {name}!"
def calculate(a, b):
    return a + b, a - b, a * b, a / b, a // b, a % b

lambda_add = lambda x, y: x + y

print(calculate(5, 3))
print(greet("Aung Aung"))
print(greet())  # using default parameter

print("Lambda Add:", lambda_add(10, 20))