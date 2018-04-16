m=int(input("enter m:"))
n=int(input("enter n:"))
for i in range(n):
    for j in range(m):
        sum=i+j
        if sum%2!=0:
            print("o",end="")
        else:
            print("*", end="")
    print() #in xong xuong dong
