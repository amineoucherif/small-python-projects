#Python Projects for beginners
#Rock, Paper, Scissors Game
#https://www.codementor.io/ilyaas97/6-python-projects-for-beginners-yn3va03fs#rock-paper-scissors-game

import random
elements=['Rock','Paper','Scissor']
computerchoiche=random.choice(elements)
print computerchoiche
userchoice=raw_input("Choice Rock, Paper, or Scissor: ")
C=computerchoiche
U=userchoice
while C==U:
    print "You did the same choices : Equality"
    break
while C!=U:
    if C=="Rock" and U=="Paper":
        print "You won."
        break
    elif C=="Rock" and U=="Scissor":
        print "Computer won."
        break
    elif C=="Scissor" and U=="Rock":
        print "You won."
        break
    elif C=="Scissor" and U=="Paper":
        print "Computer won."
        break
    elif C=="Paper" and U=="Rock":
        print "Computer won."
        break
    elif C=="Paper" and U=="Scissor":
        print "You won."
        break
    elif U!="Rock" or U!="Paper" or U!="Scissor":
        print "Verify the spelling of what you choiced !"
        break
