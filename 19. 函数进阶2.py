# 函数的参数类型

# 加
def add(x,y):
    return x+y

# 减
def substract(x,y):
    return x-y

# 乘
def multiply(x,y):
    return x*y

# 除法
def divide(x,y):
    return x/y

# 计算
def calc(x,y,oper):
    return oper(x,y)

print(calc(10,20,add))
print(calc(10,20,substract))
print(calc(10,20,multiply))
print(calc(10,20,divide))


# 匿名函数

# 定义匿名函数
# lambda 参数列表 : 函数体

# 需求1. 打印一个分割线
# def out_line():
#     print("--------------------------------")

out_line = lambda : print("--------------------------------")
out_line()

# 需求2. 计算两个数字之和
# def calc_sum(x,y):
#   return x+y

add = lambda x,y:x+y
print(add(10,20))

# 需求3. 完成如下列表的排序操作，按照每一个元素的字符个数，从小到大排序
data_list = ["C++", "C", "Python", "Jack", "PHP", "Java", "Go", "JavaScript", "Rust"]
print(data_list)

data_list.sort(key=lambda x:len(x))
print(data_list)

# 翻转 --> reverse可以控制排序是正序排序还是倒序排序
data_list.sort(key=lambda x:len(x),reverse=True)
print(data_list)


# 命名函数&匿名函数的选择

# 建议使用匿名函数的情况：
# 函数逻辑简单，只在一个地方调用（常作为高阶函数的参数）

# 建议使用命名函数的情况：
# 函数逻辑复杂，需要多次调用，或者需要加函数文档说明


print()
print("------------------------------------- 案例 -------------------------------------")
print()

# example

# 案例1：定义一个函数，根据传入的数字，计算该数字阶乘的结果
# n! = n * (n-1)!

# 递归调用（先层层递进，再逐层回归）：函数调用自身 --> 一定要考虑递归的结束条件
def factorial(n):
    # n! = n * (n-1)!
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

result = factorial(5)
print(f"5的阶乘为：{result}")


# 案例2：定义一个函数，用于根据传入的一批商品信息（商品名、价格、数量）、优惠（优惠券、积分抵扣）、运费信息计算订单的总金额
# 具体规则如下：
# 1. 优惠券需要商品金额满5000才可以使用，且优惠券金额不能超过商品总价
# 2. 积分抵扣需要商品总金额满5000才可以使用，100积分抵扣1元（且抵扣金额不能超过商品总价，积分只能整百抵扣）

def calc_order_price(*goods_list,coupon=0,score=0,express_fee=0):
    """

    :param goods_list: 商品信息（商品名、价格、数量） ----> 如: ("鼠标", 188, 2) ("键盘", 388, 1)
    :param coupon: 优惠券
    :param score: 积分
    :param express_fee: 快递运费
    :return: 订单总金额
    """

    # 1. 计算商品总金额
    total_price = [goods[1] * goods[2] for goods in goods_list]
    total_cost = sum(total_price)

    # 2. 减扣优惠券
    if total_cost >= 5000 and coupon <= total_cost:
        total_cost -= coupon
        print(f"使用优惠券，优惠了：{coupon}")

    # 3. 减扣积分
    if total_cost >= 5000 and score // 100 <= total_cost:
        total_cost -= score // 100
        print(f"使用积分，优惠了：{score // 100}")

    # 4. 添加运费
    total_cost += express_fee

    return total_cost

# 测试
cost = calc_order_price(("鼠标", 188, 20), ("键盘", 388, 1),("手机", 11899, 1), coupon=500, score=4000, express_fee=9.9)
print(f"本次消费总金额为：{cost}")