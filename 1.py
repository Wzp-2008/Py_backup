import os
import platform
v = platform.version()
print("Microsoft Windows [版本 %s.295]\n(c) 2019 Microsoft Corporation。保留所有权利。"%v)
while True:
    i = str(input("%s>"%os.getcwd()))
    if len(i) == 2 and i[1] == ":":
        os.chdir(i)
    else:
        os.system(i)
