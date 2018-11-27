# Title: To check whether a year is leap year or not 
#### Name:Yashpal Kondgule M 31


year =int(input("enter year:"))   ### user input
  # leap year check 
if  year%4==0 and year%100!=0:                #if statement
     print(year, "is a leap year")

elif year%400==0:                               #elif statement
      print(year," is a leap year")
else:                                                    # else statement
      print(year,"is not a leap year") 

