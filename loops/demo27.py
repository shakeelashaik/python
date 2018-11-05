a=0
b=0
for x in range(1,11):
    va=int(input("enter no:"))
    if va>a:
        if va>b:
            b=a
            a=va
        else:
            a=va
            b=a
print("first no is",a)
print("second is",b)
