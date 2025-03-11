from turtle import *
from math import sin, cos
scale = 10

def h_shape(t):
    x = 16 * sin(t) ** 3
    y = 13 * cos(t) - 5 * cos(2 * t) - 2 * cos(3 * t) - cos(4 * t)
    return x, y


tr = Turtle()
tr.hideturtle()
tr.penup()

tr.lt(90)
tr.goto(scale * h_shape(0)[0], scale * h_shape(0)[1])
tr.pendown()
tr.fillcolor('red')
tr.begin_fill()

scale = 10
dt = [float(i) / 10 for i in range(65)]
for t in dt:
    tr.goto(scale * h_shape(t)[0], scale * h_shape(t)[1])
tr.end_fill()

done()