numbs=[2,3,4,5,6,7,7]
x=int(input("enter the number: "))
n=False
for numb in numbs:
    if numb==x:
        n=True
if n:
    print("found")
else:
    print("NA")
