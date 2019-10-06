import os
from bs4 import BeautifulSoup
def read(file):
    with open(file,"r") as files:
        return files.read()
def append_files(file,text):
    with open(file,"a") as files:
        files.write(text)
def clean_and_write(file,text):
    with open(file,"w") as files:
        files.write(text)
dq = os.getcwd()
HTML = ""
soup = BeautifulSoup(HTML,"html.parser")
soup_t = soup.prettify()
p = soup.find_all("div",class_="result-shield-container tlid-copy-target")
print(p)
clean_and_write(r"%s\Temp\server.ini"%dq,"[main]\n")
lx = input("请输入服务端类型(原版,Cauldron)：")
v = input("游戏版本：")
dq = os.getcwd()
if lx == "原版" or lx == "Cauldron":
    append_files(r"Temp\server.ini","lx=%s\n"%lx)
if v == "1.7.10" or v == "1.8" or v == "1.9" or v == "1.10.1" or v == "1.12.2" or v == "1.13" or v == "1.14" or v == "1.14.4":
    append_files(r"Temp\server.ini", "v=%s\n"%v)