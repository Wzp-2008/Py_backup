import random
r = random.randint(1000,10000)
r_s = str(r)
cs = 0
while True:
    d = ""
    cs += 1
    i = int(input("请猜数字(1000,9999)："))
    i_s = str(i)
    if i == r:
        print("猜对啦！，共用%d次"%cs)
        break
    else:
        if i > r:
            print("big")
        elif i < r:
            print("small")
        if i_s[0] != r_s[0]:
            d+="X"
        else:
            d+=i_s[0]
        if i_s[1] != r_s[1]:
            d+="X"
        else:
            d+=i_s[1]
        if i_s[2] != r_s[2]:
            d+="X"
        else:
            d+=i_s[2]
        if i_s[3] != r_s[3]:
            d+="X"
        else:
            d+=i_s[3]
        print(d)
