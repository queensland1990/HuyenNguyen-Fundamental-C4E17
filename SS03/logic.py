from getpass import getpass

while True:
    print("welcome to the world")
    username=input("enter your username: ")
    password=getpass("enter your password: ")
    if username!="huyen":
        print("wrong username !")
    else:
        if password!="code the change":
            print("wrong pass")
        else:
            print("welcome to the world")
