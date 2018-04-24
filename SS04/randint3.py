from random import randint
x=randint(0,100)
print(x)

loop=True
count=0

while loop:
    n=int(input("your guessed number? "))
    if n==x:
        print("Bingo !!!")
        loop=False
    elif x>n:
        print("too small")
        count+=1
    if x<n:
        print("too large")
        count+=1
    if count==3:
        print("no user")
        loop=False
