import csv_all
Password_c = 0
while True:
    Users = csv_all.read("username_password.csv")
    dj = csv_all.read("username_password_dj.csv")
    zhdj = False
    User_Name = str(input("请输入用户名："))
    Password = ""
    UserName = False
    for i in dj:
        for i2 in i:
            if User_Name == i2:
                print("账户被冻结！")
                zhdj = True
        for i in Users:
            for i2 in i:
                if i2 == User_Name:
                    Password = str(i[1])
                    UserName = True
        if UserName == False:
            print("用户名错误！")
            continue
    if zhdj == False:
        Password_i = str(input("请输入密码："))
        if Password_i != Password:
            Password_c += 1
            if Password_c >= 2:
                if Password_c != 4:
                    print("密码错误%d次，再错%d次，账户将会被冻结"%(Password_c,4-Password_c))
                else:
                    print("密码错误4次，账户被冻结！")
                    Password_c = 0
                    csv_all.add("username_password_dj.csv",[User_Name])
                    break
            else:
                print("密码错误%d次"%Password_c)
        else:
            print("登录成功！")
            Password_c = 0
            breakpoint
            
