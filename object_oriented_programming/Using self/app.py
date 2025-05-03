# =============================================
# 1. Using self (Instance Methods)
# Create a class Student with attributes name and marks. 
# Use the self keyword to initialize these values via a constructor. 
# Add a method display() that prints student details.
# =============================================

class Student:
    def __init__(self, name, marks):
        self.name = name  # 'self' refers to the current instance
        self.marks = marks
    
    def display(self):
        print(f"Student: {self.name}, Marks: {self.marks}")

# Test
s1 = Student("Quratulain", 85)
s1.display()  
