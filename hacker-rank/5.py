def is_leap(year):
# to get the year from the user
    #leap = False 
    if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
        return True    
    else:
        return False

year= int (input ("Enter year: "))
print (is_leap(year))
   

  