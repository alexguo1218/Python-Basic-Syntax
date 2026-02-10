# 导入模块 --> 调用方式：模块名.功能名 / 别名.功能名
import random
import random as rd

for i in range(100):
    print(rd.randint(1, 100))


# 导入模块中的特定功能 from 模块名 import 功能名 --> 调用方式：功能名 / 别名
from random import randint
from random import randint as rint

for i in range(100):
    print(rint(1, 100))


# 导入模块中的所有功能
from random import *

for i in range(100):
    print(randint(1, 100))