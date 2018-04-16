list=["T-shirt","Sweater","Jeans"]
print("Welcome to our shop, what do you want ?")
print("update position: 2")
print("new item ? ",end="")
list[1]="Skirt"
print(list[1])
print("our items: ",end="")
print(*list,sep=", ")
