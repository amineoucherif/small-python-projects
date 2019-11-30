#Python Projects for beginners
#Hangman
#https://www.codementor.io/ilyaas97/6-python-projects-for-beginners-yn3va03fs#hangman

import random
lines = open('sowpods.txt').read().splitlines()
iterator=iter(lines)
for i in range(0,3):
    myline = random.choice(lines)
print myline

for ii in range(1,7):
    user = raw_input("Guess the word : ")
    if user == myline:
        print "Congratulations, Nice guess! The right answer is :",user
        break
    elif user != myline:
        print "Wrong, Try again.. This is your",ii,"attempt"
    else:
        print "Unfortunately, you achieved the number of attemps allowed to guess!"

