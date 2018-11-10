#static variyable in inheritance
class A:
    i=1000
    def m1(self):
        print("m1 of class A")
        print(A.i)
class B(A):
    def m2(self):
        print("m2 of class B")
        print(B.i)
y=B()
y.m1()
y.m2()
print(y.i)