def read(file):
    import openfiles
    csv = openfiles.read(file)
    csv = csv.split("\n")
    csv_l = [] 
    for i in csv:
        csv_l.append(i.split(","))
    return csv_l
def add(file,date):
    import openfiles
    if read(file) != [['']]:
        date_n = "\n"
        for i in date:
            date_n+=i
            date_n+=","
        date_n = date_n[0:len(date_n)-1]
        openfiles.append_files(file,date_n)
    else:
        date_n = ""
        for i in date:
            date_n+=i
            date_n+=","
        date_n = date_n[0:len(date_n)-1]
        openfiles.append_files(file,date_n)
def clean_and_write(file,date):
    import openfiles
    date_n = ""
    for i in date:
        date_n+=i
        date_n+=","
    date_n = date_n[0:len(date_n)-1]
    openfiles.clean_and_write(file,date_n) 
def c_replace(file,date,date_new):
    import openfiles
    csv_old = read(file)   
    csv_new=list(str(csv_old).replace(str(date),str(date_new)))
    clean_and_write(file,csv_new)
    

    
            
