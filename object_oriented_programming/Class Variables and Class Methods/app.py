# =============================================
# 4. Class Variables and Class Methods
# Create a class Bank with a class variable bank_name. 
# Add a class method change_bank_name(cls, name) that 
# allows changing the bank name. Show that it affects all instances.
# =============================================

class Bank:
    bank_name = "Default Bank"  # Class variable

    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name  # Affects all instances

# Test
b1 = Bank()
b2 = Bank()
Bank.change_bank_name("New Bank")
print(b1.bank_name)  # Output: New Bank
print(b2.bank_name)  # Output: New Bank
