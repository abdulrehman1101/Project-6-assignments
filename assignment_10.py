class Dog:
    def __init__(self, name, breed):
        self.name = name     # Instance variable
        self.breed = breed   # Instance variable

    def bark(self):
        # Instance method using self to access instance variables
        print(f"{self.name} says: Woof!")

# Example usage
dog1 = Dog("Buddy", "Golden Retriever")
dog1.bark()
