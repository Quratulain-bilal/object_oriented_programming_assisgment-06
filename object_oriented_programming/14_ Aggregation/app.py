# =============================================
# 14. Aggregation
# Create a class Department and a class Employee. Use aggregation
# by having a Department object store a reference to an Employee
# object that exists independently of it.
# =============================================

class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, name, employees=None):
        self.name = name
        self.employees = employees or []  # Aggregation
    
    def add_employee(self, employee):
        self.employees.append(employee)

# Test
emp1 = Employee("John")
dept = Department("IT")
dept.add_employee(emp1)  # emp1 exists independently

print(f"Department: {dept.name}, Employee: {dept.employees[0].name}")