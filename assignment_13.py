class Engine:
    def __init__(self, engine_type):
        self.engine_type = engine_type

    def start(self):
        print(f"{self.engine_type} engine started.")

class Car:
    def __init__(self, make, model, engine):
        self.make = make
        self.model = model
        self.engine = engine  # Composition: Car contains an Engine object

    def start_car(self):
        print(f"{self.make} {self.model} is starting...")
        self.engine.start()  # Accessing Engine's method through Car

# Example usage
engine = Engine("V8")  # Create an Engine object
car = Car("Ford", "Mustang", engine)  # Pass the Engine object to the Car class

car.start_car()  # Call the Car method that accesses Engine's start method
