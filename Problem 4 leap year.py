#Justin Mitchell
#3/7/2021

#Problem 4 Leap year



def isLeap(year):
    leap = False
    
    if year % 400 == 0:
        leap = True
    elif year % 100 == 0:
        leap = False
    elif year % 4 == 0:
        leap = True
    
    return leap
    
lYear = isLeap
print(lYear)




#I could not get this one to return a value, I believe I have the correct formula to calculate a leap year but the value is not being returned.
