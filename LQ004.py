from turtle import *
speed(0)
up()
begin_poly()
for i in range(5):
    fd(150)
    rt(72)
end_poly()
d = 1
s = 2
reset()
speed(5)
down()
begin_fill()
color("yellow")
for i in range(2):
    goto(get_poly()[s])
    s+=2
for i in range(2):
    goto(get_poly()[d])
    d+=2
goto((0,0))
end_fill()
done()
