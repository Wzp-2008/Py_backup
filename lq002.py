a = []
for i in range(1,1000):
    num = ""
    if "33" in str(i):
       num += "&"    
    if "3" in str(i):
        num+=str(i)
    for i2 in range(1,i):
        if i%i2 == 0:
           a.append(i2)
        if len(a) == 2:
            num += "*"
            break
    print(num)
