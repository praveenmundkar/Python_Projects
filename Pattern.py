try :
    n=int(input("no of row in pattern"))
    o=0
    l=[]
    bool_var=bool(int(input("type 1 for asending pattern and 0 for decending pattern ")))

    while n > 0:
        o = o + 1
        l.append(o * "*")
        if o == n:
            break
    if bool_var== True:
        for i in l :
            print(i,end="\n")
    elif bool_var== False:
        for m in l[::-1]:
            print(m)
    else :
        print("entr 0 or 1 only no other input please")
    print("if u want to print again press y or n for no")
    # h=str(input())
    # if h== str("y"):
    #     continue
    # else :
    #     break

except Exception :
    print("unaccepted input\nplease entr a valid input")
