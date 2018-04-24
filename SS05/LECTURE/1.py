p={
    "x":1,
    "y":1
}

# bx=2
# by=2
b={
    "x":2,
    "y":2
}
px=p.get('x')
py=p.get('y')
bx=b.get('x')
by=b.get('y')
while True:
    for y in range(4):
        for x in range(4):
            if x==px and y==py:
                print("P",end="")
            elif x==bx and y==by:
                print("B", end='')
            elif x==1 and y==3:
                print("G",end="")
            else:
                print("-", end="")
        print()

    move=input("your move(D/A/S/W) ?").upper()

    next_px=px
    next_py=py

    dx=0
    dy=0

    if move=='D':
        # next_px+=1
        dx=1
    elif move=="A":
        # next_px-=1
        dx=-1
    elif move== "S":
        # next_py+=1
        dy=1
    elif move=="W":
        # next_py-=1
        dy=-1

    next_px +=dx
    next_py +=dy

    if next_px==bx and next_py==by:
            bx+=dx
            by+=dy

    if 0<=next_px<4:
        px=next_px
    if 0<=next_py<4:
        py=next_py
