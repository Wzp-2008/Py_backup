import csv_all
while True:
    UserName = str(input("请输入用户名："))
    Password_1 = str(input("请输入密码："))
    Password_2 = str(input("请再次输入密码："))
    if Password_1 == Password_2:
        print("注册成功！")
        csv_all.add("username_password.csv",[UserName,Password_1])
    else:
        print("两次密码不一致！")
    
