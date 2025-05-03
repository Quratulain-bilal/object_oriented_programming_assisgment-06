# =============================================
# 9. Abstract Classes and Methods
# Use abc module to create an abstract class Shape with 
# abstract method area(). Inherit a class Rectangle that 
# implements area().
# =============================================

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):  # Must implement abstract method
        return self.length * self.width

# Test
rect = Rectangle(5, 4)
print(rect.area())  # Output: 20
