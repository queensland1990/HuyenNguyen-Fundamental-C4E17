n=int(input("enter the number of rows: "))
for i in range(n):
    for j in range(n):
        if j>i:
            print("*",end="")
        else:
            print("",end="")
    print()
