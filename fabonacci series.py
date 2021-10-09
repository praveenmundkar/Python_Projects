# 0 1 1 2 3 5 8 13 21 ......


def fabonacci(k):
    if k == 1:
        return 0
    if k == 2:
        return 1
    else:
        return fabonacci(k-1) + fabonacci(k-2)


def user_input():
    n = int(input("Type the number of which u want the fabonacci of OR press q to quit the program"))
    if n == "q":
        quit()
    else:
        print(fabonacci(n))
        print("\n")
        x = input("Type q to exit or enter to continue\n")
        if n == "q":
            quit()
            user_input()
        else:
            user_input()


user_input()
