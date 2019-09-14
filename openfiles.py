#import os
def read(file):
    with open(file,"r") as files:
        return files.read()
def append_files(file,text):
    with open(file,"a") as files:
        files.write(text)
def clean_and_write(file,text):
    with open(file,"w") as files:
        files.write(text)
#def clen_file(file):
    #os.system("del /F /Q /S %s"%file)
