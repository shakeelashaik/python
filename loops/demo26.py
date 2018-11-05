positive = 0
negative = 0
for x in range(1,11):
    va=int(input("enter no:"))

    if va>0:
        positive=positive+1
    else:
        negative=negative+1
print("no of positive numbers is",positive)
print("no of negative numbers is",negative)