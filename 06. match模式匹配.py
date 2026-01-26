# match...case 模式匹配
# example
# --> 工作日程安排
day = input("请输入今天星期几（1-7）：")

match day:
    case "1":
        print("周一：工作会议日")
    case "2":
        print("周二：学习培训日")
    case "3":
        print("周三：项目开发日")
    case "4":
        print("周四：代码审查日")
    case "5":
        print("周五：总结规划日")
    case "6" | "7":
        print("周末：休息放松日")
    case _:
        print("输入有误，请重新再试")


# example
# --> 计算器
num1 = float(input("请输入第一个数："))
num2 = float(input("请输入第二个数："))
oper = input("请输入运算符 ( + - * / )：")

match oper:
    case "+":
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    case "-":
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    case "*":
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    case "/" if num2 != 0: # if条件成立，才匹配这个case --> 因为0不能作除数
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    case _:
        print("数学错误...")