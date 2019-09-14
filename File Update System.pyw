from os import system as s
from openfiles import read as r
from os import chdir as c
c(r"C:\Users\wzp\PycharmProjects\Python\项目")
a = r(r"C:\Users\wzp\PycharmProjects\Python\Git.ini").split("\n")
U_n = a[0]
E_m = a[1]
while True:
    s("git config --global user.name %s"%U_n)
    s("git config --global user.email %s"%E_m)
    s("git add .")
    s("git commit -m \"python_backup\"")
    #s("git remote add origin https://github.com/CongliYin/CSS.git")
    s("git push origin master")