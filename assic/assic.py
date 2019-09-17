def En(file):
    import string
    big = string.ascii_uppercase
    small = string.ascii_lowercase
    with open(file)as read:
        a = read.read()
    for i in a:

    with open(file,"w") as write:
En("a")