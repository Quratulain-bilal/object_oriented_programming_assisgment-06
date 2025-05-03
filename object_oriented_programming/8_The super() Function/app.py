
# =============================================
# 8. The super() Function
# Create a class Person with name. Inherit a class Teacher 
# from it, add subject field, and use super() to call the 
# base class constructor.
# =============================================

class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # Call parent's __init__
        self.subject = subject

# Test
t = Teacher("Dr. Smith", "Physics")
print(f"{t.name} teaches {t.subject}")