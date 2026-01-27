# 字典dict
# --> 储存键值对（key: value）类型的数据，可以根据键（key）找到对应的值（value）
# 键（key）不能重复，也不可以修改；但是值（value）可以修改

# 定义字典dict
dict1 = {"王林":670, "李慕婉":608, "徐立国":500, "韩立":680}

print(dict1)
print(type(dict1))

# 定义空字典
dict2 = dict()
print(type(dict2))
# 也可以像下面这样
dict3 = {}
print(type(dict3))

# key必须是不可变类型(str,int,float,tuple)，不能是list,set,dict
# dict2 = {0:670, 1.5:608, (1,2):580, ['A', 'B']:688} # --> 这个会报错，因为它使用了list作为key
# print(dict2)

# 访问dict
print(dict1["李慕婉"])

# 修改dict --> value是可以修改的 (key不能修改)
dict1["李慕婉"] = 612
print(dict1["李慕婉"])


print()
print("------------------------------ 字典dict 常见操作 ------------------------------")
print()

dict4 = {"王林":670, "李慕婉":608, "徐立国":580, "韩立":688}
print(dict4)


# 添加 --> key不存在就是添加（存在就是修改）
dict4["涛哥"] = 550
print(dict4)


# 修改 --> key存在就是修改
dict4["涛哥"] = 620
print(dict4)


# 查询
print(dict4["涛哥"]) # --> 根据key获取value

print(dict4.get("涛哥")) # --> 根据key获取value



print(dict4.keys()) # 获取所有的key

print(dict4.values()) # 获取所有的value

print(dict4.items()) # 获取所有的键值对 key:value


# 删除
# 方法一: --> pop(key)
score = dict4.pop("徐立国")
print(f"徐立国的分数是：{score}")
print(dict4)

# 方法二： --> del dict[key]
del dict4["韩立"]
print(dict4)



# 遍历

print()
# 方法一： --> 自研
for s in dict4:
    print(f"\t{s} \t分数：{dict4[s]}")

print()
# 方法二： --> 标答 --> 使用keys()获取所有的keys
for k in dict4.keys():
    print(f"{k}:{dict4[k]}")

print()
# 方法三： --> 标答 --> 使用items()获取所有的键值对
for j in dict4.items():
    print(f"{j[0]}:{j[1]}")

print()
# 方法四： --> 标答 --> 使用items()获取所有键值对 + 解包获取到的键值对
for v, p in dict4.items():
    print(f"{v}:{p}")



print()
print("------------------------------ 字典dict 案例 ------------------------------")
print()

"""

    开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能。系统使用嵌套字典结构储存商品数据，通过控制台菜单与用户交互。
    具体功能如下：
        1. 添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
        2. 修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
        3. 删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
        4. 查询购物车：将购物车中的商品信息展示出来，格式为："商品名称: xxx, 商品价格: xxx, 商品数量: xxx"。
        5. 退出购物车
    
    结构：shopping_cart = {"Meta90":{"price":6999, "num":2}, "鼠标":{...}}
    
"""

shopping_cart = {}
menu = """
########## 购物车系统 ##########
#        1. 添加购物车         #
#        2. 修改购物车         #
#        3. 删除购物车         #
#        4. 查询购物车         #
#        5. 退出购物车         #
##############################
"""

# 1. 制作菜单

print("欢迎使用购物车管理系统")

# 2. 执行具体的操作

Run = True

while Run:

    print()
    print(menu)
    choice = input("请选择要执行的操作:")

    match choice:
        case "1":  # 1. 添加购物车
            GoodsName = input("请输入商品名称:")
            GoodsPrice = input("请输入商品价格:")
            GoodsNum = input("请输入商品数量:")

            # 如果商品已经存在于购物车，则不执行添加任务，输出提示信息
            if GoodsName in shopping_cart:
                print("该商品已存在，请重新选择~")
            else:
                shopping_cart[GoodsName] = {"price": GoodsPrice, "num": GoodsNum}
                print("商品添加完毕~")

        case "2":  # 2. 修改购物车
            GoodsName = input("请输入要修改信息的商品的名称:")

            # 如果商品不存在于购物车，则不执行修改任务，输出提示信息
            if GoodsName not in shopping_cart:
                print("该商品不存在，请重新选择~")
                continue

            GoodsPrice = input("请输入该商品最新的价格:")
            GoodsNum = input("请输入该商品最新的数量:")

            shopping_cart[GoodsName] = {"price": GoodsPrice, "num": GoodsNum}
            print("商品信息修改完毕~")

        case "3":  # 3. 删除购物车
            GoodsName = input("请输入要删除的商品的名称:")

            # 如果商品不存在于购物车中，则不执行删除任务，输出提示信息
            if GoodsName not in shopping_cart:
                print("该商品不存在，请重新选择~")
            else:
                del shopping_cart[GoodsName]
                print("商品删除完毕~")

        case "4":  # 4. 查询购物车
            for GoodsName in shopping_cart:
                GoodsInfo = shopping_cart[GoodsName]
                print(f"商品名称：{GoodsName}, 商品价格：{GoodsInfo['price']}, 商品数量：{GoodsInfo['num']}")

        case "5":  # 5. 退出购物车
            str = input("确定要退出购物车吗? -- 请输入“确认” -->")
            if str == "确认":
                Run = False
        case _:  # 匹配其他所有情况
            print("非法操作，不支持...")

print("您已成功退出购物车")



