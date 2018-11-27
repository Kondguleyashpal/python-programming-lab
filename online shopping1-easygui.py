from easygui import *             # Importing easy gui  library 
import sys
while 1:                             # while 1 loop
 msgbox("WELCOME TO ONLINE SHOPPING!")
 msg ="WhICH SITE WOULD YOU PREFER?"
 title = "ONLINE DIWALI SHOPPING"
 choices = ["amazon", "flipkart", "myntra", "snapdeal"]
 choice = choicebox(msg, title, choices)
 #msgbox("You chose: " + str(choice), "please press ok")
 if choice=="amazon":                          # nested if loop 
    msg1="what do you want on this diwali"
    title1="ONLINE DIWALI SHOPPING"
    choices1=["electronics","tv","clothes","sports"]
    choice1=choicebox(msg1,title1,choices1)
   # msgbox("You chose: " + str(choice1), "please press ok")
    if choice1=="electronics":                          # nested if loop      
       msg2="what do you want on this diwali"
       title2="ONLINE DIWALI SHOPPING"
       choices2=["mobile","computer","laptop"]
       choice2=choicebox(msg2,title2,choices2)
      # msgbox("You chose: " + str(choice2), "please press ok")
       if choice2=="mobile":                                          # nested if loop    
            msg3="select the brand"
            title3="ONLINE DIWALI SHOPPING"
            choices3=["asus","samsung","oneplus"]
            choice3=choicebox(msg3,title3,choices3)
           # msgbox("You chose: " + str(choice3), "please press ok")
            if choice3=="asus":                                            # nested if loop      
                 msg4="please select the model"
                 title4="ONLINE DIWALI SHOPPING"
                 choices4=["asus1","asus2"]
                 choice4=choicebox(msg4,title4,choices4)
                # msgbox("You chose: " + str(choice4), "please press ok")
    elif choice1=="clothes":                                                  # nested if loop 
         msg2="what do you want on this diwali"
         title2="ONLINE DIWALI SHOPPING"
         choices2=["jeans","trousers","shirts"]
         choice2=choicebox(msg2,title2,choices2)
        # msgbox("You choose: " + str(choice2), "please press ok")
         if choice2=="jeans":                                                                 # nested if loop 
                msg3="select the brand"
                title3="ONLINE DIWALI SHOPPING"
                choices3=["nike","pantaloons","levis"]
                choice3=choicebox(msg3,title3,choices3)
               # msgbox("You chose: " + str(choice3), "please press ok")
                if choice3=="levis":                                                   # nested if loop 
                     msg4="please select the model"
                     title4="ONLINE DIWALI SHOPPING"
                     choices4=["size=xl","size=xxl"]
                     choice4=choicebox(msg4,title4,choices4)
                    # msgbox("You chose: " + str(choice4), "please press ok")
    elif choice1=="tv":                                                          
         msg2="select the brand of the tv"
         title2="ONLINE DIWALI SHOPPING"
         choices2=["sony","samsung","panasonic"]
         choice2=choicebox(msg2,title2,choices2)
         #msgbox("You choose: " + str(choice2), "please press ok")
    if choice1=="sports":
       msg2="what do you want on this diwali"
       title2="ONLINE DIWALI SHOPPING"
       choices2=["racket","cricket bat","basketball"]
       choice2=choicebox(msg2,title2,choices2)
      # msgbox("You chose: " + str(choice2), "please press ok")
       if choice2=="basketball":
            msg3="select the brand"
            title3="ONLINE DIWALI SHOPPING"
            choices3=["adidas","nike"]
            choice3=choicebox(msg3,title3,choices3)
 elif choice=="flipkart":
      msg1="what do you want on this diwali"
      title1="ONLINE DIWALI SHOPPING"
      choices1=["electronis","fashion","home and furniture","tv","toys","clothes","sports"]
      choice1=choicebox(msg1,title1,choices1)
      #msgbox("You chose: " + str(choice1), "please press ok")
      if choice1=="electronics":
           msg2="what do you want on this diwali"
           title2="ONLINE DIWALI SHOPPING"
           choices2=["mobile","computer","laptop"]
           choice2=choicebox(msg2,title2,choices2)
          # msgbox("You chose: " + str(choice2), "please press ok")
           if choice2=="mobile":
               msg3="select the brand"
               title3="ONLINE DIWALI SHOPPING"
               choices3=["asus","samsung","oneplus"]
               choice3=choicebox(msg3,title3,choices3)
              # msgbox("You chose: " + str(choice3), "please press ok")
               if choice3=="asus":
                   msg4="please select the model"
                   title4="ONLINE DIWALI SHOPPING"
                   choices4=["asus1","asus2"]
                   choice4=choicebox(msg4,title4,choices4)
                  # msgbox("You chose: " + str(choice4), "please press ok")
      elif choice1=="clothes":
            msg2="what do you want on this diwali"
            title2="ONLINE DIWALI SHOPPING"
            choices2=["jeans","trousers","shirts"]
            choice2=choicebox(msg2,title2,choices2)
           # msgbox("You chose: " + str(choice2), "please press ok")
            if choice2=="jeans":
                msg3="select the brand"
                title3="ONLINE DIWALI SHOPPING"
                choices3=["nike","pantaloons","levis"]
                choice3=(msg3,title3,choices3)
               # msgbox("You chose: " + str(choice3), "please press ok")
                if choice3=="levis":
                     msg4="please select the model"
                     title4="ONLINE DIWALI SHOPPING"
                     choices4=["size=xl","size=xxl"]
                     choice4=choicebox(msg4,title4,choices4)
                    # msgbox("You chose: " + str(choice4), "please press ok")
      elif choice1=="tv":
         msg2="select the brand of the tv"
         title2="ONLINE DIWALI SHOPPING"
         choices2=["sony","samsung","panasonic"]
         choice2=choicebox(msg2,title2,choices2)
        #msgbox("You choose: " + str(choice2), "please press ok")
      elif choice1=="sports":
       msg2="what do you want on this diwali"
       title2="ONLINE DIWALI SHOPPING"
       choices2=["racket","cricket bat","basketball"]
       choice2=choicebox(msg2,title2,choices2)
      #msgbox("You chose: " + str(choice2), "please press ok")
       if choice2=="basketball":
            msg3="select the brand"
            title3="ONLINE DIWALI SHOPPING"
            choices3=["adidas","nike"]
            choice3=choicebox(msg3,title3,choices3)
 elif choice=="myntra":
     msg1="what do you want on this diwali"
     title1="ONLINE DIWALI SHOPPING"
     choices1=["electronis","fashion","home and furniture","tv","toys","clothes","sports"]
     choice1=choicebox(msg1,title1,choices1)
     #msgbox("You chose: " + str(choice1), "please press ok")
     if choice1=="electronics":
         msg2="what do you want on this diwali"
         title2="ONLINE DIWALI SHOPPING"
         choices2=["mobile","computer","laptop"]
         choice2=choicebox(msg2,title2,choices2)
        # msgbox("You chose: " + str(choice2), "please press ok")
         if choice2=="mobile":
              msg3="select the brand"
              title3="ONLINE DIWALI SHOPPING"
              choices3=["asus","samsung","oneplus"]
              choice3=choicebox(msg3,title3,choices3)
             # msgbox("You chose: " + str(choice3), "please press ok")
              if choice3=="asus":
                   msg4="please select the model"
                   title4="ONLINE DIWALI SHOPPING"
                   choices4=["asus1","asus2"]
                   choice4=choicebox(msg4,title4,choices4)
                   #msgbox("You chose: " + str(choice4), "please press ok")
     elif choice1=="clothes":
           msg2="what do you want on this diwali"
           title2="ONLINE DIWALI SHOPPING"
           choices2=["jeans","trousers","shirts"]
           choice2=choicebox(msg2,title2,choices2)
           #msgbox("You chose: " + str(choice2), "please press ok")
           if choice2=="jeans":
                msg3="select the brand"
                title3="ONLINE DIWALI SHOPPING"
                choices3=["nike","pantaloons","levis"]
                choice3=choicebox(msg3,title3,choices3)
                #msgbox("You chose: " + str(choice3), "please press ok")
                if choice3=="levis":
                     msg4="please select the model"
                     title4="ONLINE DIWALI SHOPPING"
                     choices4=["size=xl","size=xxl"]
                     choice4=choicebox(msg4,title4,choices4)
                     #msgbox("You chose: " + str(choice4), "please press ok")
     elif choice1=="tv":
         msg2="select the brand of the tv"
         title2="ONLINE DIWALI SHOPPING"
         choices2=["sony","samsung","panasonic"]
         choice2=choicebox(msg2,title2,choices2)
         #msgbox("You choose: " + str(choice2), "please press ok")
     elif choice1=="sports":
       msg2="what do you want on this diwali"
       title2="ONLINE DIWALI SHOPPING"
       choices2=["racket","cricket bat","basketball"]
       choice2=choicebox(msg2,title2,choices2)
      #msgbox("You chose: " + str(choice2), "please press ok")
       if choice2=="basketball":
            msg3="select the brand"
            title3="ONLINE DIWALI SHOPPING"
            choices3=["adidas","nike"]
            choice3=choicebox(msg3,title3,choices3)

 elif choice=="snapdeal":
      msg1="what do you want on this diwali"
      title1="ONLINE DIWALI SHOPPING"
      choices1=["electronis","fashion","home and furniture","tv","toys","clothes","sports"]
      choice1=choicebox(msg1,title1,choices1)
      #msgbox("You chose: " + str(choice1), "please press ok")
      if choice1=="electronics":
          msg2="what do you want on this diwali"
          title2="ONLINE DIWALI SHOPPING"
          choices2=["mobile","computer","laptop"]
          choice2=choicebox(msg2,title2,choices2)
          #msgbox("You chose: " + str(choice2), "please press ok")
          if choice2=="mobile":
              msg3="select the brand"
              title3="ONLINE DIWALI SHOPPING"
              choices3=["asus","samsung","oneplus"]
              choice3=choicebox(msg3,title3,choices3)
             # msgbox("You chose: " + str(choice3), "please press ok")
              if choice3=="asus":
                 msg4="please select the model"
                 title4="ONLINE DIWALI SHOPPING"
                 choices4=["asus1","asus2"]
                 choice4=choicebox(msg4,title4,choices4)
                 #msgbox("You chose: " + str(choice4), "please press ok")
      elif choice1=="clothes":
            msg2="what do you want on this diwali"
            title2="ONLINE DIWALI SHOPPING"
            choices2=["jeans","trousers","shirts"]
            choice2=choicebox(msg2,title2,choices2)
            #msgbox("You chose: " + str(choice2), "please press ok")
            if choice2=="jeans":
                msg3="select the brand"
                title3="ONLINE DIWALI SHOPPING"
                choices3=["nike","pantaloons","levis"]
                choice3=choicebox(msg3,title3,choices3)
                #msgbox("You chose: " + str(choice3), "please press ok")
                if choice3=="levis":
                     msg4="please select the model"
                     title4="ONLINE DIWALI SHOPPING"
                     choices4=["size=xl","size=xxl"]
                     choice4=choicebox(msg4,title4,choices4)
                     #msgbox("You chose: " + str(choice4), "please press ok")
      elif choice1=="tv":
         msg2="select the brand of the tv"
         title2="ONLINE DIWALI SHOPPING"
         choices2=["sony","samsung","panasonic"]
         choice2=choicebox(msg2,title2,choices2)
         #msgbox("You choose: " + str(choice2), "please press ok")
      elif choice1=="sports":
       msg2="what do you want on this diwali"
       title2="ONLINE DIWALI SHOPPING"
       choices2=["racket","cricket bat","basketball"]
       choice2=choicebox(msg2,title2,choices2)
      # msgbox("You chose: " + str(choice2), "please press ok")
       if choice2=="basketball":
            msg3="select the brand"
            title3="ONLINE DIWALI SHOPPING"
            choices3=["adidas","nike"]
            choice3=choicebox(msg3,title3,choices3)
    
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
