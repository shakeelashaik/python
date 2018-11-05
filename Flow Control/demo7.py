emp=input("name:")
sal=float(input("salary:"))
des=input("designation:")
if des=="manager":
   bonus=sal*20/100
   ts=bonus+sal
   print(ts)
if des=="analyst":
   bonus=sal*20%100
   ts=bonus+sal
   print(ts)
if des=="clerk":
   bonus=sal*5%100
   ts=bonus+sal
   print(ts)