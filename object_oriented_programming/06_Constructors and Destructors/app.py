# =============================================
# 6. Constructors and Destructors
# Create a class Logger that prints a message when an object 
# is created (constructor) and another message when it is 
# destroyed (destructor).
# =============================================

class Logger:
    def __init__(self):
        print("Logger object created!")  # Constructor
    
    def __del__(self):
        print("Logger object destroyed!")  # Destructor

# Test
logger = Logger()
del logger  # Explicitly call destructor
