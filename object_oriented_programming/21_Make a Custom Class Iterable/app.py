# =============================================
# 21. Make a Custom Class Iterable
# Create a class Countdown that takes a start number.
# Implement __iter__() and __next__() to make the object
# iterable in a for-loop, counting down to 0.
# =============================================

class Countdown:
    def __init__(self, start):
        self.start = start
    
    def __iter__(self):
        self.current = self.start
        return self
    
    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        else:
            self.current -= 1
            return self.current + 1

# Test
for num in Countdown(5):
    print(num)  # Output: 5 4 3 2 1

print("All 21 questions completed!")