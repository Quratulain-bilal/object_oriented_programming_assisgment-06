# =============================================
# 19. callable() and __call__()
# Create a class Multiplier with __init__() to set a factor.
# Define __call__() method that multiplies an input by the factor.
# Test it with callable() and by calling the object like a function.
# =============================================

class Multiplier:
    def __init__(self, factor):
        self.factor = factor
    
    def __call__(self, x):
        return x * self.factor

# Test
double = Multiplier(2)
print(callable(double))  # Output: True
print(double(5))         # Output: 10 (calls __call__)
