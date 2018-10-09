def factorial(x):
  n=0
  result=1
  while n<x:
   n=n+1
   result=result*(n)
  print(result)
x=int(input("enter no"))
z=factorial(x)
print(z)
