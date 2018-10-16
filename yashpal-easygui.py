from easygui import *
import sys
while 1:
 msgbox("WELCOME TO ONLINE SHOPPING!")
 msg ="WhICH SITE WOULD YOU PREFER?"
 title = "ONLINE DIWALI SHOPPING"
 choices = ["amazon", "flipkart", "myntra", "snapdeal"]
 choice = choicebox(msg, title, choices)
 msgbox("You chose: " + str(choice), "please press ok")
 if choices=="amazon":
  msg1="what do you want on this diwali"
  title1="ONLINE DIWALI SHOPPING"
  choices1=["electronis","fashion","home and furniture","tv","toys","clothes","sports"]
  choice1=choicebox(msg1,title1,choices1)
  msgbox("You chose: " + str(choice1), "please press ok")
  if choices1=="electronics":
   msg2="what do you want on this diwali"
   title2="ONLINE DIWALI SHOPPING"
   choices2=["mobile","computer","laptop"]
   choice2=choicebox(msg2,title2,choices2)
   msgbox("You chose: " + str(choice2), "please press ok")
   if choices2=="mobile":
     msg3="select the brand"
     title3="ONLINE DIWALI SHOPPING"
     choices3=["asus","samsung","oneplus"]
     choice3=(msg3,title3,choices3)
     msgbox("You chose: " + str(choice3), "please press ok")
     if choices3=="asus":
       msg4="please select the model"
       title4="ONLINE DIWALI SHOPPING"
       choices4=["asus1","asus2"]
       choice4=(msg4,title4,choices4)
       msgbox("You chose: " + str(choices4), "please press ok")
 else:
  sys.exit(0)        

    # note that we convert choice to string, in case
    # the user cancelled the choice, and we got None.
   # msgbox("You chose: " + str(choice), "please press ok")

    #msg = "Do you want to continue?"
    #title = "Please Confirm"
    #if ccbox(msg, title):     # show a Continue/Cancel dialog
       # pass  # user chose Continue
    #else:
       # sys.exit(0)
