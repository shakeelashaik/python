z=0
for x in range(7,0,-2):
    for y in range(z):
        print(end="  ")
    for y in range(x):
        print('*',end=" ")
    z+=1
    print()
z=2
for x in range(3,8,2):
    for y in range(z):
        print(end="  ")
    for y in range(x):
        print('*',end=" ")
    z-=1
    print()