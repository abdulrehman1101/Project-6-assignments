class Student:
    def __init__(self, name, marks):
        # Using self to assign parameters to instance variables
        self.name = name
        self.marks = marks

    def display(self):
        # Using self to access instance variables
        print("Student Name:", self.name)
        print("Marks:", self.marks)

# Example usage
student1 = Student("Alice", 92)
student1.display()
