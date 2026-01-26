# for 循环

# example
# --> 遍历输入的字符串
msg = input("请输入要遍历的字符串：")

for s in msg: # s 表示遍历出来的元素； msg 表示要遍历的数据
    print(f"元素：{s}")
else:
    print("遍历结束！")



# range()语句

# 1.range(end)
# --> 获取一个从0开始，不超过end的数列

# 2.range(start, end)
# --> 获取一个从start开始，不超过end的数列

# 3.range(start, end, step)
# --> 获取一个从start开始，common difference为step,不超过end的数列



# example
# --> 计算1-100所有奇数之和 --> 原始代码
sum = 0
for s in range(1, 101):
    if s % 2 != 0: # 奇数
        sum += s
else:
    print(f"1-100之间所有奇数之和为：{sum}")


# example
# --> 计算1-100所有奇数之和 --> 进阶代码
sum2 = 0
for s in range(1, 101, 2):
    sum2 += s
else:
    print(f"1-100之间所有奇数之和为：{sum2}")



# example
# --> 计算100-500之间所有3的倍数的数字之和
sum1 = 0
for s in range(100, 501):
    if s % 3 == 0:
        sum1 += s
else:
    print(f"100-500之间所有3的倍数的数字之和为：{sum1}")


# 嵌套循环

# example
# --> 根据输入的长方形长度m，宽度n来打印一个长方形

m = int(input("请输入长方形的长:"))
n = int(input("请输入长方形的宽:"))

for i in range(n):
    for j in range(m):
        print("*", end="  ")
    print() # 换行


# example
# --> 打印九九乘法表
for i in range(1,10): # 外层循环 --> 控制行
    for j in range(1,i+1): # 内层循环 --> 控制列
        print(f"{i} x {j} = {i * j}", end = "\t")
    print() # 换行


# example
# --> 根据输入的直角边的边长，打印等腰直角三角形
p = int(input("请输入等腰直角三角形的边长:"))

for i in range(1,p+1):
    for j in range(1,i+1):
        print("*", end = "  ")
    print()


# example
# --> 根据输入的数字打印对应的数字金字塔
num1 = int(input("请输入对应的数字："))

for i in range(1,num1+1):
    for j in range(1,i+1):
        print(j,end = "  ")
    print()
    

# example
# --> 打印国际象棋棋盘
length = 8
width = 8
for i in range(1,width+1):
    for j in range(1,length+1):
        if (i + j) % 2 == 0:
            print("@", end = " ")
        else:
            print("$", end = " ")
    print()