person={
    "names":"hellen",
    "ages": 28,
    "gender":"female"
}

values=list(person.values())
print(values[2]) # note: do dict ko support index nen du da chuyen ve list nhung co the ket qua ko ra kqua co dinh

# print(*person.keys())
# if "names" in person: #= if ... person.keys():
#     print("yeah")
if "hellen" in person.values():
    print("yes")
