from turtle import *
r = 255
g = 165
b = 0
import time
begin_fill()
for i in range(6):
    for i in range(4):
        fd(100)
        rt(90)
    rt(60)
color("yellow")
end_fill()
time.sleep(5)
speed(0)
up()
begin_poly()
for i in range(3):
    for i in range(5):
        fd(150)
        rt(72)
    rt(120)
end_poly()
d = 1
s = 2
reset()
speed(5)
down()
begin_fill()
for i in range(2):
    goto(get_poly()[s])
    s+=2
for i in range(2):
    goto(get_poly()[d])
    d+=2
goto((0,0))
rt(108)
i2 = 0
for i in range(2):
    i2 += 1
    goto(get_poly()[s+1])
    s+=2
for i in range(2):
    i2 += 1        
    goto(get_poly()[d+1])
    d+=2
goto((0,0))
rt(108)
for i in range(2):
    goto(get_poly()[s+2])
    s+=2
for i in range(2):
    goto(get_poly()[d+2])
    d+=2
goto((0,0))
rt(108)
color("yellow")
end_fill()
time.sleep(5)
reset()
begin_fill()
for i in range(5):
    for i in range(3):
        fd(100)
        rt(120)
    rt(72)
color("yellow")
end_fill()
