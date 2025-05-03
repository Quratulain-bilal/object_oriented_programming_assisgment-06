# =============================================
# 20. Creating a Custom Exception
# Create a custom exception InvalidAgeError. Write a function
# check_age(age) that raises this exception if age < 18.
# Handle it with try...except.
# =============================================

class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or older")
    return "Valid age"

# Test
try:
    check_age(15)
except InvalidAgeError as e:
    print(f"Error: {e}")  # Output: Error: Age must be 18 or older

