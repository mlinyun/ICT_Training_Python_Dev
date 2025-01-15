"""整型"""
a = 5
# 输出 a 的数据类型
print(type(a))
# 输出 a 的内存地址
print(id(a))
# 改变 a 的值，然后再输出 a 的内存地址
a = 6
print(id(a))  # 可以看到，当 a 的值发生改变时，其内存地址也随之改变了

"""布尔"""
# 在数字运算时，布尔类型相当于整数 0（False）和 1（True）
print(True + 5)
print(False * 3)

"""浮点"""
b = 1.1
print(type(b))
print(id(b))
c = 1.1 + 2.2
print(c)
print(round(c))
print(round(c, 2))
# round() 函数通常情况下能实现四舍五入，但有时候也会产生让你抓狂的结果
a = 1.119
print(round(a, 2))  # 目标：1.12 实际：1.12
b = 1.265
print(round(b, 2))  # 目标：1.27 实际：1.26
# 这个情况是因为十进制小数不能正确被浮点数表示

# 你可能想问，浮点数到底有没有办法获得正确的结果？
# 这时候，就该 decimal 模块闪亮登场了
# decimal 模块就可以实现快速正确的十进制浮点数计算，让我们得到正确的计算结果
from decimal import Decimal

a = Decimal("1.1") + Decimal("2.2")  # 这里需要注意的是 Deciaml() 必须是字符串形式的数字
print(a)

"""复数"""
# 复数由实数部分和虚数部分构成，可以用 a + bj，或者 complex(a,b) 表示
# 复数的实部 a 和虚部 b 都是浮点型
# 要从一个复数 z 中提取这两个部分，可使用 z.real 和 z.imag

a = 5 + 6j
print(a)  # 输出 a 的值
print(type(a))  # 输出 a 的数据类型
print(a.real)  # 输出 a 的实部
print(a.imag)  # 输出 a 的虚部
b = complex(2, 3)
print(b)  # 输出 b 的值
print(type(b))  # 输出 b 的数据类型
print(b.real)  # 输出 b 的实部
print(b.imag)  # 输出 b 的虚部

"""数字类型转换"""
# int() 函数
print(int())  # 参数为空
print(int(1))  # 十进制整数
print(int(1.1))  # 浮点数
print(int(0b101))  # 二进制整数
print(int(0o76))  # 八进制整数
print(int(0x32))  # 十六进制整数
# int() 函数在将字符串作为参数时，该字符串中的数字只能是整数
# 其他进制整数在转换时需要指定可选参数 base，默认是 10（十进制）
# 另外可以选择 0 或者 2-36，指定 0 会根据书写方式自动判断
print(int("10"))  # 字符串内是十进制整数
print(int('0b101', base=0))  # 字符串内是二进制整数
print(int('0b101', base=2))  # 字符串内是二进制整数
print(int('0o32', base=8))  # 字符串内是八进制整数
print(int('0x32', base=16))  # 字符串内是十六进制整数

# float() 函数
# float() 可以将数字或者字符串转换到一个浮点数类型
print(float(1))
print(float(1.5))
print(float("1"))
print(float("1.5"))
# 将字符串 "3.1415926" 转换为整数类型
a = int(float("3.1415926"))
print(a)

# complex() 函数
c = complex(a)
print(c)  # 输出 c 的值
print(c.real)  # 输出 c 的实部
print(c.imag)  # 输出 c 的虚部

# 数字运算
print(3 + 5)  # 加法
print(9 - 3)  # 减法
print(3 * 5)  # 乘法
print(10 / 3)  # 除法
print(10 // 3)  # 整除，向下取整
print(10 % 3)  # 取余，除法运算之后返回余数
print(2 ** 10)  # 乘方，2 的 10 次方

# Python 完全支持混合运算：当一个二元算术运算符的操作数有不同数值类型时
# "较窄"类型的操作数会拓宽到另一个操作数的类型，其中整数比浮点数窄，浮点数比复数窄
# 不同类型的数字之间的比较，同比较这些数字的精确值一样
a = 5
b = 3.1
c = complex(3)
d = a + b
e = a + c
print(type(d))
print(type(e))
