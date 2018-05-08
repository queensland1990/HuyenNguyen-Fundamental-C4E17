from random import randint, choice
from eval import calc
x=randint(1,10)
op=choice(['+','-','*','/'])
y=randint(1,10)
result=eval.calc(x,y,op)

err=choice([-1,0,0,0,1])
display_res= result + err
print("*"*20)
print("{0}{1}{2}={3}".format(x,op,y,display_res))
print("*"*20)

answer=input("Y/N: ").upper()
if err==0:
    if answer=="n":
        print("ahihi")
    else:
        print("sorrry")
else:
    if answer=="y":
        print("sorrry")
    else:
        print("ahihi")
