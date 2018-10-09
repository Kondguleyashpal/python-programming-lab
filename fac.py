def factors(m):
  for i in range (1,m+1):
    if (m%i==0):
      print (i,end =',')
m=int(input("enter no."))
factors(m)
