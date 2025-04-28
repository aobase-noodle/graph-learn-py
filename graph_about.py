from turtle import *

def draw_ceil(begin, y, s):
    penup()
    goto(begin, y)
    pendown()
    draw_square("black",begin-10, y+30, begin + 25, y)
    draw_title(s, 12, "black", begin+10, y+5)
    
def draw_ceil_seat(begin,y,s):
    penup()
    goto(begin, y)
    pendown()
    goto(begin+18,y)
    draw_title(s, 12, "black", begin+10, y+5)

def draw_seat(begin,y,on):
    penup()
    goto(begin, y)
    pendown()
    goto(begin+18,y)
    if on:
        title = "1"
    else:
        title = "0"
    draw_title(title, 12, "black", begin+10, y+5)
    

def draw_circuit_part(begin,y, on):
##    penup()
##    goto(begin+60,y)
##    pendown()
##    seth(90)
##    if on:
##        fillcolor("yellow")
##        begin_fill()
##    circle(10)
##    if on:
##        end_fill()
##    penup()
##    goto(begin+55,y+8)
##    pendown()
##    goto(begin+45,y-8)
##    penup()
##    goto(begin+45,y+8)
##    pendown()
##    goto(begin+55,y-8)

    draw_switch(on,begin-60,y,1)

def draw_circuit(begin,on):
    penup()
    goto(begin,0)
    pendown()
    goto(begin-23,0)
    penup()
    goto(begin-85,0)
    pendown()
    goto(begin-100,0)
    goto(begin-100,60)
    goto(begin-10,60)
    penup()
    goto(begin-5,60)
    pendown()
    goto(begin-5,80)
    goto(begin-5,40)
    penup()
    goto(begin,60)
    pendown()
    goto(begin,70)
    goto(begin,50)
    penup()
    goto(begin+5,60)
    pendown()
    goto(begin+100,60)
    goto(begin+100,0)
    goto(begin+60,0)
    seth(90)
    if on:
        fillcolor("yellow")
        begin_fill()
    circle(10)
    if on:
        end_fill()
    penup()
    goto(begin+55,8)
    pendown()
    goto(begin+45,-8)
    penup()
    goto(begin+45,8)
    pendown()
    goto(begin+55,-8)
    penup()
    goto(begin+40,0)
    pendown()
    goto(begin,0)

    draw_switch(on,begin-60,0,1)

def draw_switch(on, x,y,scale):
    pencolor("black")
    w = 2
    width(w)
    penup()
    r = 3*scale
    line_len = 20*scale
    space = 10 * scale
    goto(x-r-line_len,y)
    pendown()
    goto(x-r,y)
    seth(-90)
    circle(r)
    penup()
    goto(x+2*r+space,y)
    pendown()
    goto(x+2*r+space+line_len,y)
    penup()
    pencolor("red")
    goto(x, y+r+w)
    pendown()
    if on:
        seth(0)
        forward(line_len)
    else:
        seth(45)
        forward(line_len)
        seth(0)
    width(1)
    pencolor("black")

def draw_title(title,s,color,l,t):
    pencolor(color)
    penup()
    t_width = s * len(title)
    goto(l - t_width/2,t)
    pendown()
    write(title, font=("Arial",s,"normal"))
    pencolor("black")

def draw_square(color,l,t,r,b):
    pencolor(color)
    penup()
    goto(l,t)
    pendown()
    goto(r,t)
    goto(r,b)
    goto(l,b)
    goto(l,t)
    
def draw_area(l,t,r,b,title,s):
    area_color = "red"
    title_l = (l + r) / 2
    title_t = t + 10
    draw_title(title,s,area_color,title_l,title_t)
    draw_square(area_color,l,t,r,b)

def draw_memory(l,t,r,b,title,s):
    memory_color = "black"
    title_l = (l + r) / 2
    title_t = t + 10
    draw_title(title,s,memory_color,title_l,title_t)
    draw_square(memory_color,l,t,r,b)

def draw_memory_bot(l,t,r,b,title,s):
    memory_color = "black"
    title_l = (l + r) / 2
    title_t = b - s * 2
    draw_title(title,s,memory_color,title_l,title_t)
    draw_square(memory_color,l,t,r,b)


    
