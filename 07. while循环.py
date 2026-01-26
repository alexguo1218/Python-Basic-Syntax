# while循环

# example
# --> 打印10遍"I love wcy~"

i = 0
while i < 10:
    print("I love wcy~")
    i += 1
else:
    print("循环正常结束...")


# example
# --> 计算1-100之间所有偶数的累加之和
num = 1
sum = 0

while num <= 100:
    if num % 2 == 0:
        sum += num
    num += 1
else:
    print(f"sum = {sum}")