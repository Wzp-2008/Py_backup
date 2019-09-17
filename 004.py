import random
r = random.randint(1000,9999)
cs = 0
while True:
    d = ""
    cs += 1
    i = int(input("请猜数字(1000,9999)："))
    if i == r:
        print("猜对啦！，共用%d次"%cs)
        break
    else:
        if i > r:
            print("big")
        elif i < r:
            print("small")
        for i2 in str(i):
            i3_w = 0
            for i3 in str(r):
                i3w = i3
            if i2 == i3w:
                d += i2
            elif i2 != i3w:
                d += "X"
        print(cs)
                
            
                    
