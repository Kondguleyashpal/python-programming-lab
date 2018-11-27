#Title:Armstrong Number
#Name:Yashpal Kondgule M 31


def armstrong_no(x): #defining a function 
 s=0
 z=x
 while x>0:  # while loop
   y=x%10    # % gives a remainder 
   s+=y**3
   x=x//10    # // gives quotient
 print(s)  
 if s==z:
  print("armstrong number")
 else:                                # exits while loop
  print("not an armstrong number") 


