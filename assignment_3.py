class Car:
    def __init__(self, brand):
        # Public variable
        self.brand = brand

    # Public method
    def start(self):
        print(f"{self.brand} car has started.")

# Instantiate the class
my_car = Car("Toyota")

# Access public variable
print("Car Brand:", my_car.brand)

# Call public method
my_car.start()
