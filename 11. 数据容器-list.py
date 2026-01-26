# 列表操作
# 定义
s = [56, 90, 88, 65, 90, "A", "Hello", True]

print(type(s))

# 访问列表元素
# 获取
print(s[0]) # 正向索引 --> 从0开始
print(s[-1]) # 反向索引 --> 从-1开始

print(s[2])
print(s[-6])

# 修改
s[5] = "ABC"
print(s)

# 如果指定的索引超出范围将会报错
# s[10] = "DEF"
# print(s)

# 删除
del s[6]  # --> 删除list中正向索引为6的元素
print(s)

# 遍历
for item in s:
    print(item, end = " ")
print()

print("--------------------------列表list 切片--------------------------")

# --------------------------列表list 切片--------------------------
# 切片：对操作的数据截取其中一部分的操作

# 语法：序列数据[开始索引:结束索引:步长]
# --> 切片中不包含结束索引对应的元素
# --> 开始索引未指定则默认为0；结束索引未指定则默认为列表长度（直到列表末尾）；步长未指定默认为1
# --> 索引采用正向、反向索引都可以
# --> 步长是选取间隔（common difference），默认步长为1


# 定义列表
s1 = ["A", "C", "H", "K", "L", "B", "D", "X", "C", "U"]

# 切片操作 --> s[开始索引:结束索引:步长]
print(s1[0:5:1])
print(type(s1[0:5:1]))

# 简化操作
print(s1[:5:])
print(s1[:5]) # 第二个冒号可以省，第一个不可以

print(s1[0:5:2])
print(s1[0:-2:1])


print("--------------------------列表list 常用方法--------------------------")

# --------------------------列表list 常用方法--------------------------

# 定义列表
s2 = [56, 90, 88, 65, 90, 100, 209, 72, 145]
print(s2)

# append()：在列表尾部追加元素
s2.append(188)
print(s2)

# insert()：在指定索引之前插入元素
s2.insert(2, 80)
print(s2)

# remove()：移除列表中第一个匹配到的元素
s2.remove(90)
print(s2)

# pop()：删除列表中指定索引位置的元素并返回（如果未指定，则默认删除最后一个）
e = s2.pop(1)
print(s2)
print(e)

e = s2.pop()
print(s2)
print(e)

# sort()：排序
s2.sort()
print(s2)

# reverse()：翻转列表元素
s2.reverse()
print(s2)



print("--------------------------列表list 案例--------------------------")

# --------------------------列表list 案例--------------------------
# example
# -->  案例1. 将用户输入的10个数字储存到一个列表中，并将列表中的数字进行排序，输出其中的最小值、最大值和平均值

list1 = [] # 定义一个空列表，等待用户输入

for i in range(10): # 循环输入
    num = int(input("请输入列表元素："))
    list1.append(num)

list1.sort() # 排序 --> 升序

# 输出最大值
Max = list1[-1]  # --> 也可以使用函数 --> Max = max(list1)
print(f"list1中的最大值是{Max}")

# 输出最小值
Min = list1[0]  # --> 也可以使用函数 --> Min = min(list1)
print(f"list1中的最小值是{Min}")

# 输出平均值 --> 循环求和
# mean_value = 0
# for i in range(len(list1)):
#     mean_value += list1[i]
# mean_value /= 10
# print(f"list1中的平均值是{mean_value}")

# 输出平均值 --> sum()求和
mean_value = sum(list1) / len(list1)
print(f"list1中的平均值是{mean_value}")


# example
# --> 合并两个列表中的元素，并对合并的结果进行去重处理（去除列表中的重复元素）
num_list1 = [19, 23, 54, 64, 875, 20, 109, 232, 123, 54]
num_list2 = [55, 80, 72, 35, 60, 123, 54, 29, 91]

# 1. 合并列表
# num_list2中的元素遍历append()到num_list1中
for i in range(len(num_list2)):
    num_list1.append(num_list2[i])

# 还有简单合并列表方法
# 方法2：--> 解包:将列表这类容器拆解为一个一个的元素
# combined_list = [*num_list1, *num_list2]

# 方法3：-->直接将列表相加
# combined_list = num_list1 + num_list2

print("合并后的原始列表：", num_list1)

# 2. 去重复记录

new_list = []
for i in num_list1:
#     方法一： --> 稍复杂，但是是自己想的，逻辑很通
#     judge = True
#     for j in new_list: # --> 循环遍历new_list检查要新加的元素是否已有
#         if i == j:
#             judge = False
#     if judge:
#         new_list.append(i)
# print("去重之后的新列表：", new_list)

# 方法二： --> 很简便，使用了函数
      if i not in new_list: # 判断元素是否已经存在于new_list中，如果存在返回True；不存在返回False
          new_list.append(i)
print("去重之后的新列表：", new_list)


# example
# --> 生成1-20的平方列表

# 方法一：
num_list3 = []
for i in range(1, 21):
    num_list3.append(i**2)
print(num_list3)

# 方法二：
# --> 列表推导式:按照一定规则快速生成列表的方法
# 语法格式1：[要插入的值 for i in 序列/列表]
num_list4 = [i**2 for i in range(1, 21)]
print(num_list4)



# example
# --> 从一个数字列表中提取所有的偶数，并计算其平方，组成一个新的列表

# --> 列表推导式:按照一定规则快速生成列表的方法
# 语法格式2：[要插入的值 for i in 序列/列表 if条件] --> 这个if条件加不加可选，如果成立就执行插入，不成立就不执行插入

num_list5 = [12, 32, 45, 77, 80, 92, 33, 57, 98, 110, 111, 122]
new_list1 = [i**2 for i in num_list5 if i % 2 == 0]
print(new_list1)