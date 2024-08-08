from turtle import*
clear()
pensize(3)
clr=["blue","brown","red","green","orange","purple"]
for i in clr:
    right(60)
    color(i)
    for j in range(4):
        forward(100)
        rt(90)
