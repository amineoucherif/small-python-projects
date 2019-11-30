#Python Projects for beginners
#Hangman
#https://www.codementor.io/ilyaas97/6-python-projects-for-beginners-yn3va03fs#hangman

import random
lines = open('sowpods.txt').read().splitlines()
iterator=iter(lines)
for i in range(0,3):
    myline = random.choice(lines)
#print myline #Showing the word generated
print "PS: Use CAPITAL Letters to write your answer."

for ii in range(1,8):
    user = raw_input("Guess the word : ")
    if user == myline:
        print "Congratulations, Nice guess! The right answer is :",user
        break
    elif user != myline:
        if ii<=6:
            print "Wrong, Try again.. This is your",ii,"attempt"
        else:
            print "Unfortunately, you achieved the number of attemps allowed for guessing the right word!"

