# tuple 元组 --> 元素可以重复，有序，不可修改

# 定义
t1 = (80, 95, 78, 50, 76, 80, 85, 20)

print(t1)
print(type(t1))

# 索引访问
print(t1[0]) # --> 正向索引
print(t1[-1]) # --> 反向索引

# 切片
print(t1[0:5:1])


# count() --> 统计元素个数
print(t1.count(80))

# index() --> 获取元素的索引（第一个对应元素的位置）
print(t1.index(80))

# 注意点：如果定义单元素的元组，单个元素之后需要加上逗号，比如(100,)
t2 = ()
print(t2)
print(type(t2))

t3 = (100,)
print(t3)
print(type(t3))


# 元组的组包与解包  --  Packing & Unpacking
# 组包(Packing) --> 将多个值合并到一个容器（元组、列表）中
# 解包（Unpacking）--> 将容器（元组、列表）解开成独立的元素，分别赋值给多个变量


tt1 = (5,7,9,10,2,23,12)
tt2 = 5,7,9,10,2,23,12

print(t1)
print(t2)

# Unpacking

# 基础解包（变量数量与容器的元素个数一致）
a,b,c,d,e,f,g = tt1
print(a,b,c,d,e,f,g)

# 扩展解包（*收集剩余的所有元素，封装于列表list中）
first, second, *other, last = tt1
print(first)
print(second)
print(other)
print(last)

*other2, last2, last1 = tt1
print(other2)
print(last2)
print(last1)


# example
# --> 现有2个变量，分别为：a = 10, b = 20,现需要将这两个变量的值进行交换，然后输出到控制台
a = 10
b = 20

tt2 = b,a # 先组包
a,b = tt2 # 再解包

# 也可以直接一行代码实现 --> a,b = b,a

print(a) # 20
print(b) # 10


# example
# --> 现有3个变量，分别为m = 100, n = 200, k = 300,现需要将这三个变量的值进行交换，将mnk分别赋值给kmn，并将其输出到控制台
m = 100
n = 200
k = 300

m,n,k = k,m,n # 先组包，再解包

print(m)
print(n)
print(k)


"""
    根据如下提供的学生成绩单，完成如下要求：
        1. 计算每个学生的总分，平均分，然后一并输出出来
        2. 统计各科成绩的最低分、最高分和平均分，然后一并输出出来
        3. 查找成绩优秀（平均分大于90）的学生，然后输出出来
"""

students = (
    ("S001", "王林", 85, 92, 78),
    ("S002", "李慕婉", 92, 88, 95),
    ("S003", "十三", 78, 85, 82),
    ("S004", "曾牛", 88, 79, 91),
    ("S005", "周轶", 95, 96, 89),
    ("S006", "王卓", 76, 82, 77),
    ("S007", "红蝶", 89, 91, 94),
    ("S008", "徐立国", 75, 69, 82),
    ("S007", "许木", 86, 89, 98),
    ("S008", "遁天", 66, 59, 72),
)

print()
# 1. 计算每个学生的总分，平均分，然后一并输出出来。 --> {avg:.1f} --> 将 {avg} 保留一位小数
print("学号\t\t 姓名\t 语文\t 数学\t 英语\t 总分\t 平均分")

# 方式一：
# for s in students: # ("S001", "王林", 85, 92, 78)
#     total = s[2] + s[3] + s[4]
#     avg = total / 3
#     print(f"{s[0]} \t {s[1]} \t {s[2]} \t {s[3]} \t {s[4]} \t {total} \t {avg:.1f}")

# 方式二：--> tuple unpacking
for id,name,chinese,math,english in students: # 把students这个tuple给解包掉，后面就可以直接用解包后的元素了（如果你觉得用索引访问tuple内的元素比较麻烦）
    total = chinese + math + english
    avg = total / 3
    print(f"{id} \t {name} \t {chinese} \t {math} \t {english} \t {total} \t {avg:.1f}")


print()
# 2. 统计各科成绩的最低分、最高分和平均分
# 2.1 获取到各科的成绩列表
chinese_scores = [s[2] for s in students]
math_scores = [s[3] for s in students]
english_scores = [s[4] for s in students]

print()
# 2.2 统计各科成绩的最低分、最高分和平均分并输出
print(f"语文最低分:{min(chinese_scores)}, 最高分:{max(chinese_scores)}, 平均分:{sum(chinese_scores)/len(chinese_scores)}")
print(f"数学最低分:{min(math_scores)}, 最高分:{max(math_scores)}, 平均分:{sum(math_scores)/len(math_scores)}")
print(f"英语最低分:{min(english_scores)}, 最高分:{max(english_scores)}, 平均分:{sum(english_scores)/len(english_scores)}")

print()
# 3. 查找成绩优秀（平均分大于90）的学生并输出

print("优秀学生名单：")

# 方法一：
# for s in students:
#     total_score = s[2] + s[3] + s[4]
#     avg_score = total_score / 3
#     if avg_score > 90:
#         print(f"学号:{s[0]}, 姓名:{s[1]},平均分:{avg_score:.1f}")

# 方法二： --> tuple unpacking
for id,name,chinese,math,english in students: # 把students这个tuple给解包掉，后面就可以直接用解包后的元素了（如果你觉得用索引访问tuple内的元素比较麻烦）
    total_score = chinese + math + english
    avg_score = total_score / 3
    if avg_score > 90:
        print(f"学号:{id}, 姓名:{name},平均分:{avg_score:.1f}")

