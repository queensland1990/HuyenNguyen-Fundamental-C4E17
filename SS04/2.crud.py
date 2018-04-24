# menu=['com','pho','chao','mien',3]
# print(*menu)
#
# #create
# print("after update, we have: ")
# menu.append('pizza')
# print(*menu)
#
# #indexing
# for i in range(len(menu)): # in range chi cho ket qua int, khac voi for xxxx in others (menu, list ....)
#     print(i+1, menu[i])
#
# #for each:
# for i in menu:
#     print(i)
#
# #for enum
# for i, j in enumerate(menu): #index mac dinh dung truoc
#     print(i+1, j)
#
#
name="Hellen"
age="25"
status="single"
address="Wisconsin"
message='''{0},
handsome, tinh trang quan he:{2}, song o: {3}'''.format(name, age, status, address) # '''can be use to have new line, if you use", use \n
print(message)
# print(name+", " + str(age)+"year old" + " tinh trang: "+ status+":" + address)
