class Logger:
    def __init__(self):
        print("Logger object created. (Constructor called)")

    def __del__(self):
        print("Logger object destroyed. (Destructor called)")

# Example usage
log = Logger()

# Optional: explicitly delete the object to see the destructor in action
del log
