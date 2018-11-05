def sleep_in(weekday,vaction):
    if weekday=="False" and (vaction=="False" or vaction=="True"):
        return True
    else:
        return False
weekday=input("enter weekday:")
vaction=input("enter vaction:")
res=sleep_in(weekday,vaction)
print(res)