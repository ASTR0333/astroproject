from turtle import *
left(90)
down()
tracer(0)
m = 30
for i in range(4):
    forward(10*m)
    right(90)
up()
forward(3*m)
left(90)
forward(5*m)
right(90)
down()
for i in range(2):
    forward(10*m)
    right(90)
    forward(12*m)
    right(90)

up()
for x in range(-100,100):
    for y in range(-100,100):
        setpos(x*m,y*m)
        dot(3,'red')


done()
