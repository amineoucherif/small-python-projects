#Python Projects for beginners
#rock, paper, scissors Game
#https://www.codementor.io/ilyaas97/6-python-projects-for-beginners-yn3va03fs#rock-paper-scissors-game

import random
elements=['rock','paper','scissor']
computerchoice=random.choice(elements)
#print computerchoice
userchoice=raw_input("Choice rock, paper, or scissor: ")
C=computerchoice
U=userchoice
while C==U:
    print "You did the same choices : Equality"
    break
while C!=U:
    if C=="rock" and U=="paper":
        print "You won."
        break
    elif C=="rock" and U=="scissor":
        print "Computer won."
        break
    elif C=="scissor" and U=="rock":
        print "You won."
        break
    elif C=="scissor" and U=="paper":
        print "Computer won."
        break
    elif C=="paper" and U=="rock":
        print "Computer won."
        break
    elif C=="paper" and U=="scissor":
        print "You won."
        break
    elif U!="rock" or U!="paper" or U!="scissor":
        print "Verify the spelling of what your answer !"
        break
