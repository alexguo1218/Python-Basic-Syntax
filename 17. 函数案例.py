print()
print("--------------------------- 函数基础案例 ---------------------------")
print()


# example

# 案例1：定义一个函数：根据传入的底和高计算三角形的面积(三角形面积 = 底 * 高 / 2)
def triangle_area(l,h):
    """

    :param l: 底
    :param h: 高
    :return: 三角形面积
    """
    area = l * h / 2
    return area
print(f"底为5，高为4的三角形的面积为:{triangle_area(5,4)}")


# 案例2：定义一个函数，根据传入的字符串，统计其中元音字母的数量(元音字母为aeiou,AEIOU)
def count_vowel(s):
    count = 0
    for i in s:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
            count += 1
    return count

str = input("请输入一个字符串:")
num_vowel = count_vowel(str)
print(f"该字符串中的元音字母共有:{num_vowel}个")


# 案例3：定义一个函数：计算传入的班级学员高考成绩列表中成绩的最高分、最低分和平均分（保留一位小数），并返回
def calc_grade(grade_list):
    """

    :param grade_list: 分数列表
    :return: 最高分，最低分，平均分
    """
    max_score = max(grade_list)
    min_score = min(grade_list)
    avg_score = round(sum(grade_list)/len(grade_list),1)

    return max_score, min_score, avg_score

sample_list = [589,609,605,485,746,164,467,647,534]

max_score, min_score, avg_score = calc_grade(sample_list)
print(f"该列表中的最高分为:{max_score};最低分为:{min_score};平均分为:{avg_score}")