from easygui import *
import sys
while 1:
    msgbox("Hello, world!")

    msg ="What is your favorite colour?"
    title = "colour selection survey"
    choices = ["red","yelllow", "green", "Royal blue"]
    choice = choicebox(msg, title, choices)

    # note that we convert choice to string, in case
    # the user cancelled the choice, and we got None.
    msgbox("You chose: " + str(choice), "Survey Result")

    msg = "Do you want to continue?"
    title = "Please Confirm"
    if ccbox(msg, title):     # show a Continue/Cancel dialog
        pass  # user chose Continue
    else:
        sys.exit(0)
