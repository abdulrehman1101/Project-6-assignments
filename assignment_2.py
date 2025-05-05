class Counter:
    count = 0  # Class variable to track object count

    def __init__(self):
        # Increment count each time an object is created
        Counter.count += 1

    @classmethod
    def display_count(cls):
        # Class method using cls to access the class variable
        print("Number of Counter objects created:", cls.count)

# Example usage
c1 = Counter()
c2 = Counter()
c3 = Counter()

Counter.display_count()
