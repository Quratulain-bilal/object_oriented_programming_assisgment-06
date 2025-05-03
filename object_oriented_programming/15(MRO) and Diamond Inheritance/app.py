# =============================================
# 15. Method Resolution Order (MRO) and Diamond Inheritance
# Create four classes: A with show(), B and C that inherit from A
# and override show(), D that inherits from both B and C.
# Create an object of D and call show() to observe MRO.
# =============================================

class A:
    def show(self):
        print("A's show")

class B(A):
    def show(self):
        print("B's show")

class C(A):
    def show(self):
        print("C's show")

class D(B, C):
    pass

# Test
d = D()
d.show()  # Output: B's show (due to MRO)
print(D.mro())  # Shows method resolution order
