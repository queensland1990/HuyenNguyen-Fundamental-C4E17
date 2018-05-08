x=int(input("your number"))
y=int(input("your number: "))
op=input("your calculation *+,-,*,:")
if op == '+':
    result=x+y
elif op=='-':
    result=x-y
elif op=='*':
    result=x*y
elif op=="/":
    result = x/y
print (x,op,y,"=",result)
print("{0} {1} {2}={3}".format(x,op,y,result))
print("*"*20)

# x=int(inout("your numbers ? "))
# y=int(input("your numbers ? "))
# op=input("your calculation ? *,+,_,/ ")
# result=0
# if op=="*":
#     result=x*y
# elif op=="/":
#     result=x/y
# elif op=="+":
#     result=x+y
# elif op=="-":
#     result=x-y
# print("{0}{1}{2}={3}".format(x,op,y,result))
