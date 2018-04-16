from getpass import getpass #import getpass
while True:
    u=input("username ?")
    p=getpass("password ?") #getpass.getpass("....")
    if u=="c4e":
        if p=="code the change":
            print("welcome")
        else:
            print("your password is not correct")
    else:
        print("your user is not correct")
        break #to get out of while  true:
print(hello)
