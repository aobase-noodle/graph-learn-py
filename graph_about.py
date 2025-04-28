from turtle import *

def draw_title(l, t, s):
    pencolor("black")
    penup()
    char_size = len()
    goto(l,t)
    pendown()
    write("内存模型", font=("Arial",s,"normal"))

def draw_square(color,l,t,r,b):
    pencolor(color)
    penup()
    goto(l,t)
    pendown()
    goto(r,t)
    goto(r,b)
    goto(l,b)
    goto(l,t)
    
def draw_area(l,t,r,b):
    draw_square("red",l,t,r,b)

def draw_memory(l,t,r,b):
    draw_square("black",l,t,r,b)


    
