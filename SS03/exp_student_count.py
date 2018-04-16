students=[("Huyen,["comp","math"]"),("An",["math", "physic"])]
counter=0
for (name, subjects) in students:
    if "math" in subjects:
        counter+=1
    print("the number of students takes maths is", counter)
