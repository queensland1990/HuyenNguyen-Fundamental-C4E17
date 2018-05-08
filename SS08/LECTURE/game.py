from random import *
x=randint(1,10)
y=randint(1,10)
op = ['+','-','*','/']
choice_op = choice(op)
error=randint(-1,1) # muon tang xuat xuat dung thi phan error cho nhieu ko len  err=choice([1,0,0,0,1e])
if op == '+':
    result=x+y
elif op=='-':
    result=x-y
elif op=='*':
    result=x*y
elif op=="/":
    result = x/y
result_error=x/y+error
print("{0} {1} {2} = {3}".format(x,choice_op,y,result_error))
a=input("your answer (Y/N) ?").upper()
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
