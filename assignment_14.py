class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def display_employee(self):
        print(f"Employee: {self.name}, Role: {self.role}")


class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []  # List to store employee objects

    def add_employee(self, employee):
        # Add an Employee object to the department
        self.employees.append(employee)

    def display_department(self):
        print(f"Department: {self.department_name}")
        for emp in self.employees:
            emp.display_employee()


# Example usage
emp1 = Employee("Alice", "Software Engineer")
emp2 = Employee("Peter", "Data Scientist")

dept = Department("Technology")
dept.add_employee(emp1)
dept.add_employee(emp2)

dept.display_department()
