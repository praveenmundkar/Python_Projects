import random
import sys

list_1 = ["snake", "gun", "water"]
try :
    print("Shall we begin  the Game\n")
    x = input("PRESS   yes or no :::: IF U PRESS 'no' GAME APPLICATION will be EXITED")
    print("_________________________________________________")
    if x == "no":
        print("Thank YOU for Visiting the game")
        sys.exit()
    print("u have 10 chances:::result will be according")

    def colored(r, g, b,text):
        return "\033[38;2;{};{};{}m{} \033[38;2;;255;255;255m".format(r, g, b, text)

    def Game():
        n = 0
        v = 10
        t = 0
        w = 0

        if x == "yes":

            while n < 10:
                c = random.choice(list_1)

                print("remaining chances",v)
                v=v-1
                n=n+1

                user_inp = input("what do u want to select"
                                 "TYPE  snake or "
                                 "  gun or"
                                 " water")
                if c == user_inp:
                    print("This round has been a tie")
                    t = t+1
                    print("The computer chosen ", colored(255, 0, 0, c))
                elif c == "snake" and user_inp == "gun":
                    w = w+1
                    print("U WON this Round")
                    print("The computer chosen ", colored(255, 0, 0, c))
                elif c == "water" and user_inp == "snake":
                    w=w+1
                    print("U WON this Round")
                    print("The computer chosen ", colored(255, 0, 0, c))
                elif  c == "gun" and user_inp == "water":
                    w=w+1
                    print("U WON this Round")
                    print("The computer chosen ", colored(255, 0, 0, c))
                else :
                    print("U LOST this Round")
                    print("The computer chosen ",c)
            print("U have successfully WON ",str(w) + "  rounds\n"
                                                      "\n"
                                                      "\n")

            if w > 3 :
                print(f"so as U WON  {w} Rounds i.e  more than required NUMBER of Rounds for winning ::::🚨🚨U WON")
                print(" ")
                print(" ")
            else :
                print(f"so as U WON  {w} Rounds i.e  LESS  than required NUMBER of Rounds for winning ::::🚨🚨U LOST\n"
                      f"\n"
                      f"\n")

            q = input("do u wanna play again pess y for yes and n for no")
            while True:
                if q == "y":
                    Game()

                elif q == "n"  :
                    print("Thank YOU for Visiting the game")
                    break
                else :
                    print("given wrong input")

        else:
            print("INCORRECT INPUT🥶🥶🥶 \n \n")
        q = input("do u wanna play again pess y for yes and n for no")
        while True:
            if q == "y":
                Game()

            elif q == "n":
                print("Thank YOU for Visiting the game")
                break
            else:
                print("given wrong input")
                break

    Game()

except Exception:
    print("something went wrong in input\n\n\n")
    q = input("do u wanna play again pess y for yes and n for no")
    while True:
        if q == "y":
            Game()

        elif q == "n":
            print("Thank YOU for Visiting the game")
            break
        else:
            print("given wrong input")