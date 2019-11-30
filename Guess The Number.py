#Python Projects for beginners
#Guess The Number
#https://www.codementor.io/ilyaas97/6-python-projects-for-beginners-yn3va03fs#guess-the-number

import random
randomn=random.randint(1,20)
#print randomn
guessedn=int(input("Enter a number between 0 and 20 :"))
if guessedn==randomn:
             print "Congratulation, your guess is true :=)"
elif guessedn>randomn:
             print "You have been high from the right number!"
elif guessedn<randomn:
             print "You have been low from the right number!"
