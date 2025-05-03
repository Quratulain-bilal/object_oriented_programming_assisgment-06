# =============================================
# 12. Static Methods
# Create a class TemperatureConverter with a static method
# celsius_to_fahrenheit(c) that returns the Fahrenheit value.
# =============================================

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

# Test
print(TemperatureConverter.celsius_to_fahrenheit(30))  # Output: 86.0

