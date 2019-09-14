import turtle
import random
import time
turtle.Canvas = (800,600)
for i in range(5):
    turtle.color("black")
    x = random.randint(0, 400)
    y = random.randint(0, 200)
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    f = random.randint(10, 150)
    turtle.pensize(5)
    turtle.speed(7)
    turtle.begin_fill()
    for i2 in range(5):
        turtle.fd(f)
        turtle.lt(144)
    turtle.color("Yellow")
    turtle.end_fill()
time.sleep(5)