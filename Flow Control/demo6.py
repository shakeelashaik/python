na=input("name:")
sl=input("slab:")
un=int(input("units:"))
if sl=="industry":
    total=(un*5.25)
    print(total)
if sl=="commercial":
    total=(un*4.00)
    print(total)
if sl=="residence":
    total=(un*3.08)
    print(total)