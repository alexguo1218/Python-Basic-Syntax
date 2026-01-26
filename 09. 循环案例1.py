"""

    案例1： 根据输入的用户名和密码执行登录操作，具体要求如下：
        1. 正确的用户名和密码为admin/666888,alex/123456,wcy/888666
        2. 输入用户名和密码进行登录，直到登录成功，程序结束运行；如果登录失败，则继续输入用户名和密码进行登录
        3. 输入的用户名和密码不能为空
        4. 登陆成功：输出"登陆成功"
        5. 登录失败：输出"用户名或密码错误，请重新输入"

"""


while True:

    username = input("请输入用户名：")
    password = input("请输入密码：")

    if username == "" or password == "":
        print("用户名和密码不能为空，请重新输入")
    elif username == "alex" and password == "123456":
        break
    elif username == "wcy" and password == "888666":
        break
    elif username == "admin" and password == "666888":
        break
    else:
        print("用户名或密码错误，请重新输入")

print("登陆成功，进入B站首页~")