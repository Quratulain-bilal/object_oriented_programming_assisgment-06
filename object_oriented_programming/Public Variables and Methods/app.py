
# 3. Public Variables and Methods
# Create a class Car with a public variable brand 
# and a public method start(). Instantiate the class 
# and access both from outside the class.
# =============================================

class Car:
    def __init__(self, brand):
        self.brand = brand  # Public variable
    
    def start(self):  # Public method
        print(f"{self.brand} started!")

# Test
my_car = Car("Toyota")
print(my_car.brand)  # Access public variable
my_car.start()       # Call public method