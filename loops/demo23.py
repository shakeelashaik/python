no=int(input("enter no:"))
for x in range(2,no):
    if no%x==0:
     print(no,"is not prime number")
     break
else:
    print(no,"is prime number")