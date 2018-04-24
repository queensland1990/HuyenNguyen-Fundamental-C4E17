loop=True
count=1
while loop:
    user=input("username ?")
    password=input("your password ?")

    if user!="hellen":
        print("wrong user")
        count+=1
    elif password!="wisconsin":
        print("wrong pass")
        count+=1
    else:
        print("welcome")
        loop=False
    if count>2:
        loop=False
