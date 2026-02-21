from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass # no implementation, just a placeholder

    @abstractmethod
    def perimeter(self):
        pass

    def info(self):
        print("This is regular method in Shape class")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return 3.14 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14 * self.radius
    

c = Circle(5)
print(f"Area of Circle: {c.area()}")
print(f"Perimeter of Circle: {c.perimeter()}")
c.info()