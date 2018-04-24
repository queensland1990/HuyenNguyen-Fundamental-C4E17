# person=["hellen",40,"single","hanoi",2,11]
# print(person)
person={
    "name": "Quan",
    "age": 40,

}
#read
# print(person['name'])

# #update
# person["age"]=22
# print(person)
#
# #create
# person["home"]="Hanoi"
# print(person)
#
# #delete
#del person['age']
# print(person)
# #
# # if "home" in person: #apply to string and new_list
#     print(person["home"])
# else:
#     print("'home' is not in person")

# print(*person.keys())
# print(*person.values())

for value in person.values():
    print(value)

for key, value in person.items():
    print(key, ":", value)
