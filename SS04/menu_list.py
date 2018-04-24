menu=["pho",'comrang',"myxao"]
#for i (chay chi so)
# for i in range(len(menu)): # i mean in
#     print(i+1, menu[i])

#for each (chay gia tri)
# for item in menu:
#     print(item)

# #for enum (chay ca gia tri vaf chi so)
# for i, item in enumerate(menu):
#     print(i+1,".",item)

# name="hellen"
# age=33
# status="single"
# message="{0}, {1} tuoi, {0} tinh trang quan he: {2}".format(name, age, status)
# print(message)







name="hellen"
age=33
status="single"
address="cat linh, hanoi"
message='''{0},
{1}tuoi, tinh trang cua {0}: {2}'''.format(name, age, address)
print(message)
