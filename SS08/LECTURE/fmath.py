# from random import randint, choice
import evaluate
from evaluate import *
x=randint(1,10)
y=randint(1,10)
op = choice(['+','-','*','/'])

result=evaluate.calc(x,y,op)

print("{0} {1} {2}={3}".format(x,op,y,result))
a=input("your answer (Y/N) ?").upper()
error=randint(-1,1)
result_error=result+error
if error==0:
    if a=="Y":
        print("yeah")
    else:
        print("you are wrong")
else:
    if a=="N":
        print("yeah")
    else:
        print("you are wrong")
