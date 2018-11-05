bool=input("enter bool value:")
hour=float(input("hour:"))
def ptrouble(bool,hour):
    if hour >=0 and hour <=23:
        if hour < 7 or hour > 20:
            if bool=="True":
                return True
            else:
                return False
        else:
            return False
res=ptrouble(bool,hour)
print(res)