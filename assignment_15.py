class A:
    def show(self):
        print("Method show() from class A")

class B(A):
    def show(self):
        print("Method show() from class B")

class C(A):
    def show(self):
        print("Method show() from class C")

class D(B, C):
    pass

# Create an object of D
d = D()
d.show()  # Calling show() to observe MRO
