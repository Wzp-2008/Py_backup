import os
class En:
    def open_read(file):
        with open(file) as files:
            return files.read()
    def open_write(file,write):
        with open(file,"w") as files:
            files.write(write)
    class Encode:
        def Encode_c(text,file):
            a = ""
            for i in En.open_read(file):
                a+=text
            En.open_write(file,a)
        def Encode_c_all(text,files):
            os.chdir(files)
            files_l = os.listdir(files)
            for i in files_l:
                En.Encode.Encode_c(text,i)
En.Encode.Encode_c("a",r"G:\test.txt")
En.Encode.Encode_c_all("A",r"G:\test")