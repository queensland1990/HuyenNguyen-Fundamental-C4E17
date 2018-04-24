from random import  *

n=randint(0,100)
print(n)
p=True
while p:
    m=int(input("Guess your number (1,100) ?"))
    if n==m:
        print("bingo")
        p=False
    elif n-m>10:
        print("too large")
    elif 10>=n-m>0:
        print("a little bit large")
    elif -10<n-m<0:
        print("small")
    else:
        print("too small")
