from random import randint, choice

def calc(x,y,op): #def: từ khóa định nghĩa 1 funtion, calc print... đều là function do mình đặt
    # x=randint(1,10)
    # op=choice(['+','-','*','/'])
    # y=randint(1,10)
    result=0
    # op="+"

    if op=="*":
        result=x*y
    elif op=="/":
        result=x/y
    elif op=="+":
        result=x+y
    elif op=="-":
        result=x-y
    return(result)

print(__name__)

if __name__=='__main__':
    print('eval.py imported')
# print(result)

# calc(3,7,'-')
#result=calc(1,2,'+')
#print(result)
