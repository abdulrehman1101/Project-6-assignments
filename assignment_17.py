# Class decorator to add a greet() method
def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    
    # Add the greet method to the class
    cls.greet = greet
    return cls

# Apply the decorator to the Person class
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

# Example usage
person = Person("Alice")
print(person.greet())  # Calling the greet method added by the decorator
