name=input("enter name:")
no=0
for x in range(1,len(name)+1):
    for y in range(x):
        print(name[no],end=" ")
        no+=1
        if no == len(name):
            break
    if no == len(name):
        break

    print()