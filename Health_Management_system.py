import datetime

a = int(input("Press 1 to log and 2 for retreive"))


def gettime():
    return datetime.datetime.now()


def log():
    n = int(input("press 1 for exercise\n"                    
                  "       2 for food"))
    if n == 1:
        a = int(input("press 1 for harry\n"
                      "      2 for rohan\n"
                      "      3 for shyam"))
        t = input("type the log details here")
        if a == 1:
            with open("harry_ex.txt","a") as op :
                op.write(str([str(gettime())]) + " :: "+t)
                print("Succesfully written")
        if a == 2:
            with open("Rohan_ex.txt","a") as op :
                op.write(str([str(gettime())]) + " :: "+t)
                print("Succesfully written")
        if a == 3:
            with open("Shyam_ex.txt","a") as op :
                op.write(str([str(gettime())]) + " :: "+t)
                print("Succesfully written")
    if n == 2:
        a = int(input("press 1 for harry\n"
                      "      2 for rohan\n"
                      "      3 for shyam"))
        t = input("type the log details here")
        if a == 1:
            with open("harry_food.txt", "a") as op:
                op.write(str([str(gettime())]) + " :: " + t)
                print("Succesfully written")
        if a == 2:
            with open("Rohan_food.txt", "a") as op:
                op.write(str([str(gettime())]) + " :: " + t)
                print("Succesfully written")
        if a == 3:
            with open("Shyam_food.txt", "a") as op:
                op.write(str([str(gettime())]) + " :: " + t)
                print("Succesfully written")


def retrieve():
    n = int(input("press 1 for exercise\n"
                  "       2 for food"))
    if n == 1:
        a = int(input("press 1 for harry\n"
                      "      2 for rohan\n"
                      "      3 for shyam"))
        if a == 1:
            with open("harry_ex.txt") as op:
                print(op.read())
        if a == 2:
            with open("Rohan_ex.txt") as op:
                print(op.read())
        if a == 3:
            with open("Shyam_ex.txt") as op:
                print(op.read())
    if n == 2:
        a = int(input("press 1 for harry\n"
                      "      2 for rohan\n"
                      "      3 for shyam"))
        if a == 1:
            with open("harry_food.txt") as op:
                print(op.read())
        if a == 2:
            with open("Rohan_food.txt") as op:
                print(op.read())
        if a == 3:
            with open("Shyam_food.txt") as op:
                print(op.read())


if a == 1:
    log()
elif a == 2:
    retrieve()
else:
    print("give a valid input")
