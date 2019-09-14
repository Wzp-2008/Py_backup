import random
a = ["1","3","5","8"]
num_a = []
for i in range(1000):
    num = ""
    for i in range(3):
        num+=a[random.randint(0,3)]
    num_a.append(num)
i3 = 0
for i in num_a:
    for i2 in num_a:
        if i == i2:
            num_a.pop(i3)
    i3 += 1
print(num_a)

