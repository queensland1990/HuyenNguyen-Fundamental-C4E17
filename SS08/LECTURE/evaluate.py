from random import *
# define:
def calc(x,y,op):
    # x=randint(1,10)
    # y=randint(1,10)
    # op = choice(['+','-','*','/'])

    error=randint(-1,1) # muon tang xuat xuat dung thi phan error cho nhieu ko len  err=choice([1,0,0,0,1e])

    result=0
    # op='+'

    if op == '+':
        result=x+y
    elif op=='-':
        result=x-y
    elif op=='*':
        result=x*y
    elif op=="/":
        result = x/y
    return result
# print(__name__)
#
# if __name__=="__main__":
#     print("evaluate.py imported")
# print(result)
# usage/call:
# calc(2,4,'*')
