pn=0
for x in range(1,11):
    no = int(input("enter no:"))
    for y in range(2,no):
        if no%y==0:
            break
    else:
         pn+=1
print("no of prime numbers=",pn)