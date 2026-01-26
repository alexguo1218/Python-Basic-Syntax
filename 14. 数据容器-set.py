# set集合 --> 无序、不可重复、可修改
# 应用 --> 手机号，身份证号

# 定义集合

# 定义
s1 = {5, 3, 2, 0, 9, 12, 43, 64, 22, 5, 0}

print(s1) # --> 你会发现有自动去重
print(type(s1))

s2 = {} # --> 这不是定义空集合
print(type(s2)) # --> 你会发现这个会输出<class 'dict'>，说明s2是一个字典类型的变量

# 定义空集合
s2_2 = set()
print(s2_2)
print(type(s2_2))


print("--------------------------- set 集合的常见方法 ---------------------------")

s = {100,200,300,400,500,600,700,800}
print(s)

# add() --> 添加元素到集合中
s.add(1200)
print(s)

# remove() --> 集合中指定的元素（指定元素不存在将报错）
s.remove(200)
print(s)

# pop() --> 随机删除集合中的元素并返回
e = s.pop()
print(e)
print(s)

# clear() --> 清空集合
s.clear()
print(s) # 会输出set()


ss1 = {"A", "B", "C", "D", "E", "X", "Y"}
ss2 = {"C", "E", "Y", "Z"}

print()
# difference() --> 求两个集合的差集（存在于第一个集合，但是不存在与第二个集合的元素）
print(ss2.difference(ss1)) # --> ss2有，ss1没有的元素
print(ss1.difference(ss2)) # --> ss1有，ss2没有的元素

print()
# union() --> 求两个集合的并集
print(ss2.union(ss1))
print(ss1.union(ss2))

print()
# intersection() --> 求两个集合的交集
print(ss1.intersection(ss2))
print(ss2.intersection(ss1))


# example
print()
print("-------------------------------------集合 set 案例-------------------------------------")
print()

# 选修足球学生名单
football_set = {"王林", "曾牛", "徐立国", "遁天", "天运子", "韩立", "厉飞雨", "乌丑", "紫灵"}
# 选修篮球学生名单
basketball_set = {"张铁", "墨居仁","王林", "姜老道", "曾牛", "王蝉", "韩立", "天运子", "李化元", "厉飞雨", "云露"}
# 选修法语学生名单
french_set = {"许木", "王卓", "十三", "虎咆", "姜老道", "天运子",  "红蝶", "厉飞雨", "韩立", "曾牛"}
# 选修艺术学生名单
art_set = { "遁天", "天运子", "韩立", "虎咆", "姜老道", "紫灵"}


# 1. 找出同时选修了 法语 和 艺术 的学生

# 方式一：
fa_set = french_set.intersection(art_set)
print(f"同时选修了 法语 和 艺术 的学生:{fa_set}")

# 方式二：& --> 交集
fa_set2 = french_set & art_set
print(f"同时选修了 法语 和 艺术 的学生:{fa_set2}")


# 2. 找出同时选修了所有四门课的学生
all_set = french_set & basketball_set & football_set & art_set
print(f"同时选修了4门课程的学生：{all_set}")


# 3. 找出选修了 足球 但是没有选修 篮球 的学生

# 方法一：
diff_set = football_set.difference(basketball_set)
print(f"选修了足球但是没有选修篮球的学生：{diff_set}")

# 方法二：- --> 差集
diff_set2 = football_set - basketball_set
print(f"选修了足球但是没有选修篮球的同学：{diff_set2}")

# 方法三：集合推导式 --> 快速构建集合，语法：{要往集合中添加的数据 for s in set1 if 条件}
diff_set3 = {s for s in football_set if s not in basketball_set}
print(f"选修了足球但是没有选修篮球的同学：{diff_set3}")



# 4. 统计每一个学生选修的课程数量

# 4.1 获取到学生名单 --> | 并集
# all_student_set = football_set.union(basketball_set).union(french_set).union(art_set)
# --> 有更简单的方法 --> | 这个符号表示并集
all_student_set = football_set | basketball_set | french_set | art_set # 会自动去重
print(all_student_set)

# 4.2 获取每一个学生选修的课程数量
all_list = [*football_set, *basketball_set, *french_set, *art_set] # 解包football,basketball等set

for s in all_student_set:
    print(f"{s}选修了{all_list.count(s)}门课程")