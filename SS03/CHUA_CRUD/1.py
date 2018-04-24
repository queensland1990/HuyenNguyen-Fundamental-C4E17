items=["pizza","rice","noddle","porch"]
choice=input("welcome to our shop, what do you want (C,R,U,D) ? ")
if choice=="R":
    print("our items: ", end="")
    print(*items, sep=", ")
elif choice=="C":
    new=input("enter your new items: ")
    items.append(new)
    print("our items: ",end='')
    print(*items, sep=', ')
elif choice=="U":
    position=int(input("update your position: "))
    update=input("update: ")
    items[position-1]=update
    print("our items: ",end='')
    print(*items,sep=', ')
elif choice=="D":
    deletion=int(input("delete position: "))
    items.pop(deletion-1)
    print("our items: ",end='')
    print(*items,sep=', ')
