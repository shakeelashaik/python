a = int(input("no1:"))
b = int(input("no2:"))
bool = input("bool:")
if a>0 and b<0 and bool=="False":
        print(True)
elif a<0 and b>0 and bool=="False":
        print(True)
elif a<0 and b<0 and bool=="True":
        print(True)
else:
        print(False)

