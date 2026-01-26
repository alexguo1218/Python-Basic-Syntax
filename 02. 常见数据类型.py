# 常见数据类型
# type() --> 获取指定的字面量或者变量的数据类型
print("Hello")
print(type("Hello"))  # str

print(type(10))  # int
print(type(3.14))  # float
print(type(True))  # bool
print(type(False))  # bool
print(type(None))  # NoneType


num = -100
print(type(num))  # int


# 通过isinstance()函数来检查数据是否属于指定的类型
# --> 返回的是一个bool值，具体的语法为: isinstance(数据, 类型)
print(isinstance(num, int))  # True
print(isinstance(num, float))  # False
print(isinstance(num, str))  # False
print(isinstance(num, bool))  # False


# 字符串
# 定义字符串的3种方式
s1 = "Hello"
s2 = 'Hello'
s3 = """
Hello
World
"""
print(s1)
print(s2)
print(s3)

print(type(s1))
print(type(s2))
print(type(s3))


# 定义字符串 --> It's very good --> 使用转义字符
msg = 'It\'s very good'
print(msg)

msg2 = "It's very good"
print(msg2)

msg3 = "no \"Problem\""
print(msg3)

msg4 = 'no "Problem'
print(msg4)

print("\tWelcome everyone join the python learning\n\tAnd do not forget to click likes")
# \t 缩进
# \n 换行


# 字符串拼接
s1 = "Love"
s2 = "WCY"
print("Alex says: " + s1, s2)

# example
name = "alex"
age = 17
major = "cs"
hobby = "python"
print("\n\tHello everyone, I am " + name + ".\n\tI am " + str(age) + " years old. \n\tI am major in " + major + ".\n\tMy hobby is " + hobby)


# 字符串格式化 --> 方式一 --> %s 占位符
name1 = "wcy"
age1 = 16
major1 = "finance"
hobby1 = "reading"
print("\n\tHello everyone, I am %s.\n\tI am %s years old. \n\tI am major in %s. \n\tMy hobby is %s." % (name1, age1, major1, hobby1))


# 字符串格式化 --> 方式二 --> f"内容{变量/表达式}" --> 这个非常简洁常用，建议使用
name2 = "coco"
age2 = 50
major2 = "trader"
hobby2 = "reading"
print(f"\n\tHello everyone, I am {name2}.\n\tI am {age2} years old. \n\tI am major in {major2}. \n\tMy hobby is {hobby}.")

