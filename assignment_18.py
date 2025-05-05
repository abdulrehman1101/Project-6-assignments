class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price  # Private attribute

    # Getter for price
    @property
    def price(self):
        return self._price

    # Setter for price
    @price.setter
    def price(self, value):
        if value < 0:
            print("Price cannot be negative!")
        else:
            self._price = value

    # Deleter for price
    @price.deleter
    def price(self):
        print(f"Price of {self.name} is being deleted")
        del self._price

# Example usage
product = Product("Laptop", 1000)

# Accessing price using the getter
print("Price:", product.price)

# Updating price using the setter
product.price = 1200
print("Updated Price:", product.price)

# Trying to set a negative price (invalid)
product.price = -500

# Deleting the price attribute
del product.price

# Trying to access price after deletion (will raise an error)
# print(product.price)  # Uncommenting this will raise an AttributeError
