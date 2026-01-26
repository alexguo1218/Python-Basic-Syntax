# if条件判断:如果分数超过680，我就可以去清华
score = int(input("请输入你分数:"))
if score > 680:
    print("恭喜,你可以去清华了")


# example
# 结合前面学习的输入输出及if条件判断的知识，完成B站登录功能的实现
# 正确账号和密码为：18888888888、666888

correct_account = "18888888888"
correct_password = "666888"

# 1.接收用户输入的账号和密码
account1 = input("账号:")
password1 = input("密码:")

# 2.判断账号密码是否全部正确，如果都正确，则登陆成功，进入B站首页
if account1 == correct_account and password1 == correct_password:
    print("登陆成功，欢迎进入B站")

# 3.判断账号和密码是否有错误的，如果有任何一处错误，则登录失败，提示错误信息
if account1 != correct_account or password1 != correct_password:
    print("登录失败，账号/密码错误")

print("--------------------")

# example --> 升级版 --> else:
# 结合前面学习的输入输出及if条件判断的知识，完成B站登录功能的实现
# 正确账号和密码为：18888888888、666888

correct_account = "18888888888"
correct_password = "666888"

# 1.接收用户输入的账号和密码
account1 = input("账号:")
password1 = input("密码:")

# 2.判断账号密码是否全部正确，如果都正确，则登陆成功，进入B站首页;如果有任何一处错误，则登录失败，提示错误信息
if account1 == correct_account and password1 == correct_password:
    print("登陆成功，欢迎进入B站")
else:
    print("登录失败，账号/密码错误")

# example
# --> 根据输入的年份判断是闰年还是平年
# --> 非整百年份，且能被4整除的年份是闰年
# --> 整百年份，必须被400整除才是闰年
year = int(input("请输入年份："))
if year % 100 != 0:
    if year % 4 == 0:
        print(f"{year}年是闰年")
    else:
        print(f"{year}年是平年")
else:
    if year % 400 == 0:
        print(f"{year}年是闰年")
    else:
        print(f"{year}年是平年")


# example
# --> 判断输入的数是奇数还是偶数
num = int(input("请输入一个数字："))
if num % 2 == 0:
    print(f"{num}是偶数")
else:
    print(f"{num}是奇数")


# example
# --> 判断用户是否成年
age = int(input("请输入你的年龄："))
if age >= 18:
    print("你已成年")
else:
    print("你是未成年")


# example
# --> 判断输入的数是正数还是负数（不考虑0）
in_num = int(input("请输入一个数："))
if in_num > 0:
    print(f"{in_num}是正数")
else:
    print(f"{in_num}是负数")


# example --> 升级版 --> 考虑0
# --> 判断输入的数是正数还是负数（考虑0）
in_num = int(input("请输入一个数："))
if in_num > 0:
    print(f"{in_num}是正数")
elif in_num < 0:
    print(f"{in_num}是负数")
else:
    print(f"{in_num}是0")


# example
# --> 根据输入的用户名+密码进行登录系统
# 用户名、密码为 admin/666888 或 root/123456 或 alex/999999 则输出登陆成功，否则就提示用户名或密码错误

# 正确用户名+密码
name_a, name_b, name_c = ("admin", "root", "alex")
password_a, password_b, password_c = ("666888", "123456", "999999")

# 读取输入的用户名+密码
name_input = input("用户名：")
password_input = input("密码：")

if (name_input == name_a and password_input == password_a):
    print(f"{name_a}欢迎，登陆成功")
elif (name_input == name_b and password_input == password_b):
    print(f"{name_b}欢迎，登陆成功")
elif (name_input == name_c and password_input == password_c):
    print(f"{name_c}欢迎，登陆成功")
else:
    print("账号/密码错误，请重新输入")


# example
# --> 根据输入的三角形三边长度（正整数），判断三角形类型（或者不能构成三角形）

# 1.输入三条边的长度
l1 = int(input("请输入第一条边的长度："))
l2 = int(input("请输入第二条边的长度："))
l3 = int(input("请输入第三条边的长度："))

# 2.判断三角形类型
if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1: # 条件成立，构成三角形
    # pass # 语法占位
    if l1 == l2 and l2 == l3:
        print(f"{l1} {l2} {l3}这三个边长构成等边三角形")
    elif l1 == l2 or l2 == l3 or l1 == l3:
        print(f"{l1} {l2} {l3}这三个边长构成等腰三角形")
    else:
        print(f"{l1} {l2} {l3}这三个边长构成普通三角形")
else:
    print(f"{l1} {l2} {l3}这三个边长不能构成三角形")
