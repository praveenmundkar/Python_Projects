import random

n = random.randint(1, 25)
print("u have to guess the no")
print("lets begin a game ")
print("no of guesses u have are 5")
print("u will be getting a tip after each guess that is ur no. is less than or greater than the real no")
d = 5
while(True):
    a = int(input())
    if a == n :
        print (f"congratulations u won the gme in only {6-d} guesses of"')
        break
    else :
        if a <n :
            print("the no. is greater than your guess")
        else :
            print("the no.  is less than ur guess")
        d = d-1
        print("no of guesses remaining sre ",d)
        if d == 0 :
            print("u have lost the game")
            break