import module.hello as hello

# 查看导入的 hello 模块名称
print(hello.__name__)

import module.abcd as abcd  # 全部导入

# 调用 abcd 模块中的变量和函数
x = abcd.x
y = abcd.y
print(x, y)
abcd.a()
abcd.b()
abcd.c()
abcd.d()

from module.abcd import a as funa  # 只导入 abcd 模块中的 a

# 调用 abcd 模块中的 a 函数
funa()
# 使用 from ... import * 语句可以导入全部
from module.abcd import *

x = abcd.x
y = abcd.y
print(x, y)
abcd.a()
abcd.b()
abcd.c()
abcd.d()
# 上面的这种导入虽然方便，但是官方并不建议这样导入模块
# 因为这样导入可能导致各种模块中的同名函数互相干扰

# 从包中导入 *
from module import *

# 打印 hello 模块的文件路径
print(hello.__file__)

# 调用 abcd 模块
x = abcd.x
y = abcd.y
abcd.a()
abcd.b()
abcd.c()
abcd.d()
