sunday= [8,1,2,3,4,5,6,7]
monday=[1,2,3,4,5,6,7,8]
tuesday=[2,3,4,5,6,7,8,1]
wednesday=[3,4,5,6,7,8,1,2]
satursday=[4,5,6,7,8,1,2,3]
thursday=[5,6,7,8,1,2,3,4]
friday=[7,8,1,2,3,4,5,6]

def for_age(day):
    if day=="1":
        return sunday
    elif day=="2":
        return monday
    elif day=="3":
        return tuesday
    elif day=="4":
        return wednesday
    elif day=="5":
        return satursday
    elif day=="6":
        return thursday
    elif day=="7":
        return friday

