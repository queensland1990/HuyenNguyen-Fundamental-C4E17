list=["T-shirt","Sweater"]
print("Welcome to our shop, what do you want ?")
new_list=["Jeans"]
print("enter new item: ",end="")
print(*new_list)
print("our items: ",end="")
list.append(*new_list)
print(*list,sep=", ")
