from turtle import*
def draw_star(x,y,length):
    for i in range(5):
        forward(length)
        right(x)
    return draw_star
draw_star(144,0,200)
mainloop()
