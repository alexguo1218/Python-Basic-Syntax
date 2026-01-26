# 字符串 基本操作
s = "Hello-Python"

print(s[4]) # 正向索引
print(s[-8]) # 反向索引

# s[4] = "X" --> 报错(体现了字符串的不可修改性)



# 可迭代性
for i in s:
    print(i, end = " ")


print("\n--------切片--------")
# 切片
# s[start:end:step] --> 不包含end

# 截取Hello
print(s[0:5:1])
print(s[:5:1])
print(s[:5:])
print(s[:5])

# 截取Python
print(s[6:12:1])
print(s[6:])
print(s[6::1])
print(s[6:12:])
print(s[6:12])

# 步长
print(s[0:5:2]) # step为正数 --> 从前往后截取
print(s[11:5:-1]) # step为负数 --> 从后往前截取


# --------------------------- 字符串常用方法 ---------------------------
print("--------------------------- 字符串str 常用方法 ---------------------------")

str1 = "     Hello-Python-Hello-World     "

# find() --> 查找指定字符串第一次出现的索引位置
index = str1.find("-")
print(f"在该字符串中\"-\"第一次出现在索引{index}处")

# count() --> 统计子字符串在指定字符串中出现的次数
c = str1.count("o")
print(f"在该字符串中\"o\"的次数为{c}")

# upper() --> 转为大写
str1_up = str1.upper()
print(str1_up)

# lower() --> 转为小写
str1_low = str1.lower()
print(str1_low)

# split() --> 将字符串切割(括号里的东西就是切割的地方) --> 返回一个列表
str1_list = str1.split("-")
print(str1_list)

# strip() --> 去除字符串两端的空格
str1_s = str1.strip()
print(str1_s)

# replace() --> 将字符串中的指定子串替换为新的内容
str1_r = str1.replace("-", "_")
print(str1_r)

# startswith() / endswith() --> 判断字符串是否是以指定的字符串开头/结尾的，会返回一个bool值
print(str1.startswith("Hello"))
print(str1.endswith("Python"))

print("------------------------------------------------------")
print(str1)


# --------------------------- 字符串案例 ---------------------------

# example
# --> 案例1. 邮箱格式验证：用户输入一个邮箱地址，验证邮箱格式是否正确(包含一个@和至少一个.)，如果输入正确，输出"邮箱格式正确"，否则输出"邮箱格式错误"

mail_address  = input("请输入您的邮箱地址：")

first_time = mail_address.count("@")
second_time = mail_address.count(".")

if first_time == 1 and second_time > 0: # --> 还有一个方法:对于second_time可以直接用in来判断.在不在mail_address中-->他会返回一个bool值
    print("邮箱格式正确")
else:
    print("邮箱格式错误")



