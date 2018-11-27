# Title: To check whether a year is leap year or not 
#### Name:Yashpal Kondgule M 31


year =int(input("enter year:"))   ### taking the input
  # leap year check 
if  year%4==0 and year%100!=0:
     print(year, "is a leap year")

elif year%400==0:
      print(year," is a leap year")
else:
      print(year,"is not a leap year") 

