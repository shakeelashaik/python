#example on default constructor in inheritance
class A:
    def __init__(self):
        print("Default constructor of class A")
class B(A):
    def display(self):
        print("show method of class B")
b=B()
b.display()