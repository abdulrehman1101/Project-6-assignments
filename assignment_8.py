# Base class
class Person:
    def __init__(self, name):
        self.name = name
        print(f"Person constructor called for {self.name}")

# Derived class
class Teacher(Person):
    def __init__(self, name, subject):
        # Call the constructor of the base class
        super().__init__(name)
        self.subject = subject
        print(f"Teacher constructor called for subject: {self.subject}")

    def display(self):
        print(f"Name: {self.name}")
        print(f"Subject: {self.subject}")

# Example usage
t1 = Teacher("Mr. Abdul", "Mathematics")
t1.display()
