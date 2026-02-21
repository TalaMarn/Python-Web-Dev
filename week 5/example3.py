# Polimorphism
# same operation or method to behave differently on different classes
# Two main types
# 1. Compile-time
# 2. Run-time (common) => Python support

# class Vehicle:
#     def start_engine(self):
#         print("Vehicle engine starts!")

# class Car(Vehicle):
#     def start_engine(self):
#         print("Car engine starts with a roar!")

# class Motorcycle(Vehicle):
#     def start_engine(self):
#         print("Motorcycle engine starts with a vroom!")

# Vehicle = [Car(), Motorcycle()]
# for vehicle in Vehicle:
#     vehicle.start_engine()

# Example 2

class Dog:
    def speak(self):
        print ("Woof!")

class Cat:
    def speak(self):
        print ("Meow!")

animals = [Dog(), Cat()]

for animal in animals:
    animal.speak()