class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name          # Public
        self._salary = salary     # Protected
        self.__ssn = ssn          # Private

    def show_details(self):
        print("Name:", self.name)
        print("Salary:", self._salary)
        print("SSN:", self.__ssn)

# Create object
emp = Employee("John Doe", 50000, "123-45-6789")

# Access public variable
print("Public - Name:", emp.name)  # Works

# Access protected variable
print("Protected - Salary:", emp._salary)  # Works, but not recommended (convention)

# Try to access private variable
try:
    print("Private - SSN:", emp.__ssn)  # Fails
except AttributeError as e:
    print("Error accessing private variable:", e)

# Correct way to access private variable (name mangling)
print("Private (via name mangling) - SSN:", emp._Employee__ssn)
