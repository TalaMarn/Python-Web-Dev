### Inheritence

# child -> subclass => reuse attri & methods of parent class

# add new attr & methods to child class
# override attr & methods of parent class
### syntax

class Parent:
    def greet(self):
        print("Hello from Parent class")

class Child(Parent):
    def greet(self):
        print("Hello from Child class")