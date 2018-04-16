list=["T-shirt","Sweater","Jeans"]
print("Welcome to our shop, what do you want ?")
print("delete position: 3")
del list[2]
print("our items: ",end="")
print(*list,sep=", ")
