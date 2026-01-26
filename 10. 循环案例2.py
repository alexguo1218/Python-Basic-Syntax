"""

    案例2： 猜数字游戏，具体要求如下：
        1. 系统随机生成一个随机数
        2. 用户根据提示猜数字，并将所猜的数字输入系统
        3. 如果猜错，系统给出提示是猜大了还是猜小了，然后继续输入猜的数字
        4. 如果猜对，系统自动退出，游戏结束

"""

import random

num = random.randint(1,100) # 随机生成一个1-100之间的整数
time = 0 # 猜测次数

while True:
    ans = int(input("请输入您的猜测："))
    time += 1
    if ans == num:
        print("恭喜你，猜对啦！")
        break
    elif ans > num:
        print("猜大了，再试试吧")
        continue
    elif ans < num:
        print("猜小了，再试试吧")

print(f"你一共猜了{time}次就猜对了，太厉害了")