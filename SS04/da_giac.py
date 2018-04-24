from turtle import*
speed(0)
color_list=["red","blue"]
color_n=len(color_list) # check lai de lam gi
for n in range(3,10):
    # selected_color=color_list[n-3] # ap dung truong hop nhieu may, nhung neu chi co 3 mau ma so hinh nhieu hon so mau
    selected_color=color_list[(n-2)%2]
    color(selected_color)
    for i in range (n):
        forward(100)
        left(360/n)


mainloop()
