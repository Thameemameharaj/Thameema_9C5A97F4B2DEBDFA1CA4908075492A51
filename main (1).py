# Leap year 

"""
year % 4 == 0&
year % 100:=0/
year % 400 ==0

"""
def isLeapyear(year):
 if (year % 4 == 0 and year %10!= 0) or year % 400 == 0:
  return True 
 else:
  return False

year = int(input("Enter the Year :"))

if isLeapYearYear(year):
   print('{} is a leap year.'.format( year))
else:
  print('{} is not a leap year.'.format( year))

  
