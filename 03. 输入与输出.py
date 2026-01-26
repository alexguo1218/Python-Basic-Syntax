# 获取键盘上输入的数据 -- input(...)

name = input("enter your name:")
age = input("enter your age:")

print(f"\tyour name is {name} \n\tyour age is {age}")


# example
# --> 银行卡中有1w元，现在到ATM进行取钱操作，完毕后展示银行卡余额
# --> 步骤：1.输入密码；2.输入取款金额；3.计算余额并退出
rest_money = 10000

# 1.输入密码
password = input("请输入密码:")
print(f"密码正确，{password}")

# 2.输入取款金额
num = input("请输入取款金额:")

# 3.计算余额并输出 --> num 转为 int 类型 --> int(...)
print(f"取款后银行卡余额为：{rest_money - int(num)}")

