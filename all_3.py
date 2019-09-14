n = []
for i in range(1,10):
    for i2 in range(1,10):
        for i3 in range(0,9,2):
            if i != i2 and i2 != i3 and i != i3:
                n.append(str(i)+str(i2)+str(i3))
print(n)