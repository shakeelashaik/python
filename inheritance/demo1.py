class A:
    def m1(self):
        print("m1 of class A")
class B(A):
    def m2(self):
        print("m2 of class B")
x=A()
x.m1()
y=B()
y.m1()
y.m2()