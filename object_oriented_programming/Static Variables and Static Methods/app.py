# =============================================
# 5. Static Variables and Static Methods
# Create a class MathUtils with a static method add(a, b) 
# that returns the sum. No class or instance variables should be used.
# =============================================

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b  # Doesn't use self or cls

# Test
print(MathUtils.add(5, 3))  # Output: 8
print(MathUtils.add(10, 20))  # Output: 30