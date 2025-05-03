# =============================================
# 10. Instance Methods
# Create a class Dog with instance variables name and breed. 
# Add an instance method bark() that prints a message 
# including the dog's name.
# =============================================

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def bark(self):  # Instance method
        print(f"{self.name} says Woof!")

# Test
dog = Dog("Buddy", "Golden Retriever")
dog.bark()  # Output: Buddy says Woof!