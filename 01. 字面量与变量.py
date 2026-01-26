# 字面量的写法
print(100)  # int类型
print(3.14)  # float类型
print(True)  # bool类型  --- True/False首字母必须大写
print("hello python")  # string类型
print("---------------")  # string类型
print(None)  # NoneType


# bool类型本质为int类型
# True = 1
# False = 0
print(True + 1)
print(False - 1)

# 变量
# --> python是一个动态类型语言，一个变量是可以存储不同类型的数据的
# （但是在项目开发中，推荐一个变量只储存一种类型）
num = 1114.1
print(num)

num = num + 2
print(num)

num = "OK"
print(num)

num = True
print(num)

a = True
print(a)



# example
# 基础播放量20.7w，每月新增50w，求未来两个月每个月的播放量
base = 20.7
incr = 50
print("未来第一个月的播放总量", base + incr)
print("未来第二个月的播放总量", base + incr * 2)


# example  --> 升级：一次性可以定义多个变量
# 基础播放量20.7w，每月新增50w，求未来两个月每个月的播放量
base1, incr1 = 20.7, 50
print("未来第一个月的播放总量", base1 + incr1)
print("未来第二个月的播放总量", base1+ incr1 * 2)


# example
# a, b = 10, 20 --> 交换a, b的值
a, b = 10, 20
p = a  # --> 使用一个中间变量p
a = b
b = p
print("a =", a)
print("b =", b)


# example
# a, b, c = 100, 200, 300 --> 交换abc为cab并输出
a, b, c = 100, 200, 300
p = a
q = b
a = c
b = p
c  = q
print("a =", a)
print("b =", b)
print("c =", c)