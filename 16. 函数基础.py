# 函数定义的时候并不会执行，只有在调用函数的时候，函数体的逻辑才会执行；函数必须先定义，后调用

# 函数定义

def out_line():
    print("---------------------------------")
    print("---------------------------------")

# 函数调用
out_line()


# 函数的参数与返回值
# 函数1：计算圆的面积
def circle_area(r):
    area = 3.14 * r ** 2
    return area

area = circle_area(10)
print(f"半径为10的圆的面积为：{area}")



# 函数2：计算长方形的面积 -- 长，宽
def rectangle_area(l,w):
    """
    根据长方形的长度和宽度，计算长方形的面积
    :param l: 长度
    :param w: 宽度
    :return: 长方形面积
    """
    area = l * w
    return area
help(rectangle_area)

print(f"长为20，宽为10的长方形面积为：{rectangle_area(20,10)}")


# 函数3：计算圆的面积，周长 -- 半径r --> 如果函数返回值有多个，直接return返回值，并在多个返回值之间用逗号分隔
def circle_area_len(r):
    """
    根据圆的半径计算圆的周长和面积
    :param r: 半径
    :return: 面积+周长
    """
    return 3.14 * r ** 2, round(2 * 3.14 * r, 1) # --> 使用函数round(number, ndigits) --> 四舍五入,number表示要转化的数字,ndigits表示保留的小数位数

al = circle_area_len(10)
print(al)
print(type(al)) # --> 元组 tuple

area, length = circle_area_len(10) # --> 解包元组 unpacking tuple
print(f"半径为10的圆，周长为：{length}，面积为：{area}")



# 函数的嵌套调用
def function_a():
    print("a...before")
    function_b()
    print("a...after")

def function_b():
    print("b...before")
    function_c()
    print("b...after")

def function_c():
    print("c...")

function_a()

print("函数调用完毕~")


