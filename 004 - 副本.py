from turtle import *
speed(0)
up()
begin_poly()
for i in range(9):
    for i in range(5):
        fd(150)
        rt(72)
    rt(72)
end_poly()
d = 1
s = 2
reset()
speed(5)
down()
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
i2 = 0
for i in range(2):
    i2 += 1
    goto(get_poly()[s+3])
    s+=2
for i in range(2):
    i2 += 1        
    goto(get_poly()[d+3])
    d+=2
goto((0,0))
rt(108)
for i in range(2):
    i2 += 1
    goto(get_poly()[s+4])
    s+=2
for i in range(2):
    i2 += 1        
    goto(get_poly()[d+4])
    d+=2
goto((0,0))
rt(108)
