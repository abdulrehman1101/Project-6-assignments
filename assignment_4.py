class Bank:
    # Class variable shared by all instances
    bank_name = "National Bank"

    def __init__(self, account_holder):
        self.account_holder = account_holder

    @classmethod
    def change_bank_name(cls, name):
        # Class method to change the class variable
        cls.bank_name = name

    def display_info(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Bank Name: {Bank.bank_name}")

# Create instances
acc1 = Bank("Alice")
acc2 = Bank("Bob")

# Display original bank name
acc1.display_info()
acc2.display_info()

# Change bank name using class method
Bank.change_bank_name("Mezaan Bank")

# Display updated bank name for both instances
print("\nAfter changing bank name:\n")
acc1.display_info()
acc2.display_info()
