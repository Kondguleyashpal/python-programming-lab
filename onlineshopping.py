
### Tiltle Online Shopping

### Name Yashpal Kondgule M 31




rom easygui import *         # importing easy gui library. 
import sys
while 1:
    msgbox("welcoome to online shop")

    msg ="what you want to buy?"
    title = "online shopping"
    choices = ["ashing machine", "Refrigerator"]
    choice = choicebox(msg, title, choices)

    # note that we convert choice to string, in case
    # the user cancelled the choice, and we got None.
    msgbox("You chose: " +str(choice))
    if choice=="refrigerator":
      choices1=["LG","whirlpool","samsung"]
      chose=buttonbox(choice,choices1)
      if chose=="LG":
         choices2=["165ltr.","185 ltr","170ltr."]
         chose2=buttonbox(chose,choices2)
         msgbox("you chose:"+str(chose2))
      if chose=="whirlpool":
         choices3=["170 ltr.","160 ltr.","150 ltr."]
         chose3=buttonbox(chose,choices3)
         msgbox("you chose:"+str(chose3))
      if chose=="samsung":
         choice4=["140ltr.","145 ltr.","150ltr."]
         chose4=buttonbox(chose,choices4)
         msgbox=("you chose:"+str(chose4))
    elif choice=="washing machine": ### elif condition
         choices5=["LG","samsung","videocon"]
         chose5=buttonbox(choice,choices5)
         if chose5=="LG":
            choices6=["5ltr.","6ltr.","7ltr."]
            chose6=buttonbox(chose5,choices6)
            msgbox("you chose:"+str(chose6))
         if chose5=="samsung":
            choices7=["3ltr.","4ltr.","5ltr."]
            chose7=buttonbox(chose5,choices7)
            msgbox("you chose:"+str(chose7))
         if chose5=="videocon":
            choices8=["6ltr.","6.5ltr.","7ltr."]
            chose8=buttonbox(chose5,choices8)
            msgbox("you chose:"+str(chose8))
    else:
         msgbox("Thank you for visiting")
