# 算术运算符·
print("10 + 4 =", 10 + 4)  # 加
print("10 - 4 =", 10 - 4)  # 减
print("10 * 4 =", 10 * 4)  # 乘
print("10 / 4 =", 10 / 4)  # 除
print("10 // 4 =", 10 // 4)  # 整除（结果为整数）
print("10 % 4 =", 10 % 4)  # 取余/取模
print("10 ** 4 =", 10 ** 4)  # 幂指数，10的4次方

# 算数运算符的优先级
# --> ** --> * / // % --> + -
print("0.1 + 10 / 4 ** 2 =", 0.1 + 10 / 4 ** 2)

# example
# 输入两个数x,y --> 分别输出x+y与x-y
x = float(input("请输入x:"))
y = float(input("请输入y:"))
print(f"\tx + y = {x + y}\n\tx - y = {x - y}")


# 赋值运算符
num = 85

num += 10 # num = num + 10
print("num += 10 后, num =", num) # 95

num -= 10 # num = num - 10
print("num -= 10 后, num =", num) # 85

num *= 10 # num = num * 10
print("num *= 10 后, num =", num) # 850

num /= 10 # num = num / 10
print("num /= 10 后, num =", num) # 85.0

num //= 10 # num = num // 10
print("num //= 10 后, num =", num) # 8.0

num %= 3 # num = num % 3
print("num %= 3 后, num =", num) # 2.0

num **= 3 # num = num ** 3
print("num **= 3 后, num =", num) # 8.0


print("------------------------")

# 比较运算符/关系运算符
print("100 == 100吗？ -->", 100 == 100) # True
print("'100' == '100'吗？ -->", '100' == '100') # True
print("100 != 100吗？ -->", 100 != 100) # False

print("100 < 100吗？ -->", 100 < 100) # False
print("100 <= 100吗？ -->", 100 <= 100) # True

print("100 > 100吗？ -->", 100 > 100) # False
print("100 >= 100吗？ -->", 100 >= 100) # True

print("------------------------")

# 逻辑运算符
# --> and; or; not

# example
# 键盘上录入一个整数，判断这个数字是否在10~20之间
num = int(input("请输入一个整数:"))
print(f"{num}在10~20之间吗？ -->", num <= 20 and num >= 10)

print("------------------------")

# example
# 键盘上录入一个整数，判断这个数字是否不在10~20之间
num1 = int(input("请输入一个整数："))
print(f"{num1}在10~20之间吗？ -->", num > 20 and num < 10)

