from turtle import*
def draw_square(l,c):
    for i in range (4):
        color(c)
        forward(l)
        left(90)
    left(17)
    penup()
    forward(i * 2)
    pendown()
    mainloop()
    # return draw_square
draw_square(100,"red")
