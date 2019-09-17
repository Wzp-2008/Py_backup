import csvread
import openfiles
assic = csvread.main("ASSIC.csv")
file = input("Please enter file position:")
En = ""
text = openfiles.read(file)
for i in text:
    print(i)
    for assic_t in assic.keys():
        if assic_t == i:
            print(assic_t)
            print(assic[assic_t])
            En+=assic[assic_t]
            En+="/"
print(En)
print(text)
print(assic)
openfiles.clean_and_write(file,En)