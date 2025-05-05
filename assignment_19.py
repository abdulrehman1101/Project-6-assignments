class Multiplier:
    def __init__(self, factor):
        self.factor = factor  # Set the factor to multiply

    def __call__(self, value):
        # Multiply the input by the factor
        return value * self.factor

# Example usage
multiplier = Multiplier(5)

# Check if the object is callable using callable()
print(callable(multiplier))  # True, since __call__ is defined

# Use the object as a function
result = multiplier(10)  # This calls the __call__ method
print("Result of multiplication:", result)
