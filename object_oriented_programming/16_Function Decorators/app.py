# =============================================
# 16. Function Decorators
# Write a decorator function log_function_call that prints
# "Function is being called" before a function executes.
# Apply it to a function say_hello().
# =============================================

def log_function_call(func):
    def wrapper(*args, **kwargs):
        print("Function is being called")
        return func(*args, **kwargs)
    return wrapper

@log_function_call
def say_hello(name):
    print(f"Hello, {name}!")

# Test
say_hello("Alice")  # Output: Function is being called \n Hello, Alice!