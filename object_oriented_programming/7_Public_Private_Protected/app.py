# =============================================
# 7. Access Modifiers
# Create a class Employee with:
# - public variable name
# - protected variable _salary
# - private variable __ssn
# Try accessing all three variables from an object.
# =============================================

class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name        # Public
        self._salary = salary    # Protected (convention)
        self.__ssn = ssn        # Private (name mangling)

# Test
emp = Employee("John", 50000, "123-45-6789")
print(emp.name)        # Works
print(emp._salary)     # Works but shouldn't (protected)
# print(emp.__ssn)     # Error! Private variable
