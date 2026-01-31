# 变量定义 - 常规
a = 596
score = 98.5
hobby = "Python"
flag = True
pic = None

name = ["A", "C", "E", 100]
phones = {"13995691876", "17771888232", "18888888888"}
options = {"count":2, "total":10}
goods = ("手机", 6999, 1)

name.append("X")
name.append(10010)



# 变量定义 - 类型注解
a1: int = 596
score1: float = 98.5
hobby1: str = "Python"
flag1: bool = True
pic1: None = None

name1: list[str | int] = ["A", "C", "E"]
phones1: set[str] = {"13995691876", "17771888232", "18888888888"}
options1: dict[str, int] = {"count":2, "total":10}
goods1: tuple[str, int, int] = ("手机", 6999, 1)


# 如果你定义变量的时候，没有指定类型
# ---> 那么Python会自动根据你的赋值进行类型判断



# 函数 - 类型注解
# 为函数添加类型注解，其实主要就是为函数的参数和返回值添加类型注解

def circle_area_len(r: float) -> tuple[float, float]:
    return round(3.14 * r ** 2, 1), round(2 * 3.14 * r, 1)

al = circle_area_len(10)
print(f"半径为10的圆的面积为{al[0]}，周长为{al[1]}")



# 案例2：定义一个函数，用于根据传入的一批商品信息（商品名、价格、数量）、优惠（优惠券、积分抵扣）、运费信息计算订单的总金额
# 具体规则如下：
# 1. 优惠券需要商品金额满5000才可以使用，且优惠券金额不能超过商品总价
# 2. 积分抵扣需要商品总金额满5000才可以使用，100积分抵扣1元（且抵扣金额不能超过商品总价，积分只能整百抵扣）

def calc_order_price(*goods_list:tuple[str, float, int],coupon:int=0,score:int=0,express_fee:float=0) -> float:
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