# --------------------------- 函数 - 变量的作用域 ---------------------------

# 全局变量
num = 100
num1 = 100

# 定义函数
def circle_area(r):

    # 声明num1为全局变量
    global num1
    num1 = 10000

    # 局部变量
    pi = 3.14
    area = pi * r * r

    num = 10000 # 这里并不能操作全局变量
    print(f"num = {num}")
    return area

# 调用函数
c_area = circle_area(10)
print(f"半径为10的圆的面积为:{c_area}")

print(f"num = {num}")
print(f"num1 = {num}")


# --------------------------- 函数 - 传参方式 ---------------------------

# 定义函数
def reg_stu(name,age,gender,city):
    print(f"注册成功，姓名：{name}，年龄：{age}，性别：{gender}，城市：{city}")
    return {"name":name, "age":age, "gender":gender, "city":city}

# 传参方式一：位置参数
stu1 = reg_stu("张三",18,"男","北京")
print(stu1)

# 传参方式二：关键字参数
stu2 = reg_stu(name="王林",age=28,gender="男",city="武汉")
print(stu2)

stu3 = reg_stu(age=20,gender="女",name="李慕婉",city="重庆")
print(stu3)

# 传参方式三：位置参数 + 关键字参数
stu4 = reg_stu("李斯",78,city="洛阳",gender="男")
print(stu4)


# --------------------------- 函数 - 默认参数 ---------------------------

# 定义函数
def reg_stu1(name,age,gender="男",city="武汉"):
    print(f"注册成功,姓名:{name},年龄:{age},性别:{gender},城市:{city}")
    return {"name":name, "age":age, "gender":gender, "city":city}

# 调用函数
stu5 = reg_stu1("王林",20)
print(stu5)

stu6 = reg_stu1("李慕婉",20,"女")
print(stu6)

stu7 = reg_stu1("韩立",20,city="上海")
print(stu7)


# ------------------------------ 函数 - 不定长参数（位置参数 *args --> tuple元组）------------------------------

# 需求：根据传入的这批数据，计算这批数据的最小值，最大值和平均值

def calc_data(*args): # 会把传入的数据封装到一个tuple元组中
    min_data = min(args)
    max_data = max(args)
    mean_data = sum(args)/len(args)

    return min_data, max_data, round(mean_data,1)

# 调用函数
print(calc_data(2,7,9,10,45))

print(calc_data(2,7,9,10,45,73,93,92,111,222))


# ------------------------------ 函数 - 不定长参数（关键字参数 **kwargs --> dict字典） ------------------------------

def calc_data1(*args, **kwargs):
    """

    :param args:不定长位置参数
    :param kwargs:不定长关键字参数
        round:保留的小数位数
        print:是否输出打印
    :return:最小值，最大值和平均值
    """
    min_data = min(args)
    max_data = max(args)
    mean_data = sum(args)/len(args)

    if kwargs.get("round") is not None:
        mean_data = round(mean_data, kwargs.get("round"))

    if kwargs.get("print"):
        print(f"最小值：{min_data},最大值：{max_data},平均值：{mean_data}")

    return min_data, max_data, mean_data

# 调用函数
print(calc_data1(2,7,9,10,45,round=1,print=False))

print(calc_data1(2,7,9,32,65,24,45,45,234,54,234,54,245,425,245,round=3,print=True))