even = 0
odd = 0
for x in range(1,11):
    va=int(input("enter no"))

    if va%2==0:
        even=even+1
    else:
        odd=odd+1
print("no of even numbers is",even)
print("no of odd numbers is",odd)