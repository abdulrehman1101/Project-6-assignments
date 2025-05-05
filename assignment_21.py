class Countdown:
    def __init__(self, start):
        self.start = start
        self.current = start  # Set the initial current value

    def __iter__(self):
        return self  # The object itself is the iterator

    def __next__(self):
        if self.current < 0:
            raise StopIteration  # Stop when below 0
        value = self.current
        self.current -= 1
        return value

# Example usage
cd = Countdown(5)

for number in cd:
    print(number)
