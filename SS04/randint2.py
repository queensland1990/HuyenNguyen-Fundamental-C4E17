from random import randint
x=randint(0,100)
loop=True
count=0
print(x)
while True:
    n=int(input("your guess ?"))
    if n==x:
        print("Bingo !!!")
        loop=False
    elif n>x:
        print("too small")
        count+=1
    else:
        print("too large")
        count+=1
    if count<3:
        print("out of game")
        loop=False
