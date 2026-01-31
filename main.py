# 导入模块

# import my_fun


# # 使用模块中的功能
# print(my_fun.PI)
# print(my_fun.NAME)
#
# my_fun.log_separator1()
# my_fun.log_separator3()


# 导入自定义模块中的特定功能
from my_fun import log_separator1, log_separator3, PI, NAME

# 使用模块中的功能
print(PI)
print(NAME)

log_separator1()
log_separator3()


# 如果想一次导入模块中的所有功能(__all__没有被定义时)
# from my_fun import *

