
# =============================================
# 2. Using cls (Class Methods)
# Create a class Counter that keeps track of how many objects 
# have been created. Use a class variable and a class method 
# with cls to manage and display the count.
# =============================================

class Counter:
    count = 0  # Class variable shared by all instances

    def __init__(self):
        Counter.increment()  # Call class method on instance creation

    @classmethod
    def increment(cls):
        cls.count += 1  # 'cls' refers to the class

    @classmethod
    def get_count(cls):
        return cls.count

# Test
c1 = Counter()
c2 = Counter()
print(Counter.get_count())  

