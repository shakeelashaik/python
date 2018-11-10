#static variyable in inheritance
class A:
    i=1000
    def m1(self):
        print("m1 of class A")
        print(A.i)
class B(A):
    i = 2000
    def m2(self):
        print("m2 of class B")
        print(B.i)
x=B()
x.m2()
x.m1()
print(x.i)#2000