import webbrowser
import json
#创建字典
try:
    with open("usr_data.json","r") as file:
        user_db = json.load(file)
except FileNotFoundError:
    user_db = {"123":"123"}

#注册函数
def register(usrname,password):
    if usrname in user_db.keys():
        print(f"the username {usrname} is repeat!")
    else:
        user_db[usrname] = password
        print(f"{usrname} register successfully!")
        save_user_data()

#登录函数
def login(usrname,password):
    if usrname not in user_db.keys():
        print(f"the usrname {usrname} is not registered!")
    else:
        if user_db[usrname] == password :
            print(f"{usrname} login successfully!")
        else:
            print("wrong password!")

#密码重置函数
def reset_password(usrname,new_password):
    if usrname not in user_db:
        print ("the usrname is not registered!")
    else:
        if new_password ==  user_db[usrname]:
            print ("your password is repeat!")
        else:
            user_db[usrname] = new_password
            print("you change your password successfully")
            save_user_data()

#保存用户数据
def save_user_data():
    with open("usr_data.json","w") as file:
        json.dump(user_db,file)

#登录逻辑界面
def login():
    usrname = input("请输入用户名")
    if usrname in user_db:
        password = input("请输入密码")
        if password == user_db[usrname]:
            print("登录成功！")
            url = "https://www.bilibili.com"
            webbrowser.open(url)  # 使用 webbrowser 打开指定网页
        else:
            a = input("密码错误,是否重置密码？（y/n）")
            if a == 'y':
                b = input("请输入用户名")
                c = input("请输入密码")
                reset_password(b,c)
                login()
            else:
                login()
    else:
        a = input("是否注册？(y/n)")
        if a == 'y':
            b = input("请输入用户名")
            c = input("请输入密码")
            register(b, c)
            login()
        else:
            login()

login()










#
# import hashlib
#
# # 用户数据库（字典结构）
# user_db = {}
#
# # 密码加密函数
# def encrypt_password(password):
# return hashlib.sha256(password.encode()).hexdigest()
#
# # 用户注册函数
# def register(username, password):
# if username in user_db:
# print("该用户名已被注册！")
# else:
# encrypted_password = encrypt_password(password)
# user_db[username] = encrypted_password
# print(f"用户 {username} 注册成功！")
#
# # 示例：注册用户
# register("user1", "mypassword")
# register("user1", "anotherpassword")
#
#
# # 用户登录函数
# def login(username, password):
# if username not in user_db:
# print("用户名不存在！")
# else:
# encrypted_password = encrypt_password(password)
# if user_db[username] == encrypted_password:
# print(f"欢迎，{username}！登录成功。")
# else:
# print("密码错误！")
#
# # 示例：登录系统
# login("user1", "mypassword") # 正确的密码
# login("user1", "wrongpassword") # 错误的密码
# login("user2", "mypassword") # 不存在的用户名
#
# # 密码重置函数
# def reset_password(username, old_password, new_password):
# if username not in user_db:
# print("用户名不存在！")
# else:
# encrypted_old_password = encrypt_password(old_password)
# if user_db[username] == encrypted_old_password:
# encrypted_new_password = encrypt_password(new_password)
# user_db[username] = encrypted_new_password
# print(f"用户 {username} 的密码已更新！")
# else:
# print("旧密码错误！")
#
# # 示例：重置密码
# reset_password("user1", "mypassword", "newpassword")
# login("user1", "newpassword") # 使用新密码登录