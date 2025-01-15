# 元组 tuple

"""元组的创建"""
# 使用一对圆括号来表示空元组: ()
t = ()
print(type(t))

# 使用一个后缀的逗号来表示单元组: a, 或 (a,)
t = (5)
print(t)
print(type(t))  # 缺少逗号时为整型

t = (5,)
print(t)
print(type(t))  # 加上逗号之后为元组
t = 6,
print(t)
print(type(t))  # 这种形式也是元组

# 使用以逗号分隔的多个项: a, b, c or (a, b, c)
country = "中国", "美国", "俄罗斯"
print(country)
print(tuple(country))

# 使用内置的 tuple() 或 tuple(iterable)，iterable 指可迭代对象
# 像字符串、元组、列表、字典、集合都是可迭代对象，但数字不是可迭代对象
t = tuple([1, 2, 3, 4])  # 用列表创建元组
print(t)
print(type(t))
t = tuple("abcdef")  # 用字符串创建元组
print(t)
print(type(t))

"""元组的索引和切片"""
t = ("a", "b", "c", "d", "e", "f", "g", "h")
t_0 = t[0]  # 访问元素
print(t_0)
t_02 = t[0:3]  # 切片
print(t_02)
t_re = t[::-1]  # 翻转
print(t_re)

"""元组的修改"""
# 因为元组是不可变数据类型，当我们试图通过索引去修改元组的某个元素时，将会报错
# t[0] = "A"
# 但我们有时候也会有修改数据的需求，这时候我们就可以结合 + 运算符和切片操作来实现
t = ("A",) + t[1:]  # 通过这个操作，我们可以把元组中的 a 修改成为 A
print(t)  # 需要注意，这里虽然实现了元组的修改，但此时的元组对象已经发生了变化
# 即我们本质上时新建了一个新的元组

"""元组的运算符"""
# 与字符串一样，元组也有很多可以使用的运算符，比如 +、*、in等
# + 运算符
a = (1, 2, 3)
b = (4, 5, 6)
c = a + b
print(c)
print(type(c))
# * 运算符
d = a * 3
print(d)
print(type(d))
# in 和 not in 运算符
print(1 in a)
print("1" in a)  # 注意元组的类型
print(4 not in a)

"""元组解包"""
a = 1, 2, 3  # 这是元组打包的例子，我们可以使用逆操作实现元组解包
x, y, z = a
print(x, y, z)

"""元组的常用函数和方法"""
# count() 方法可以统计某个元素的的数量
a = (1, 2, 3, 1, 5, 3, 1, 7, 8, 10)
print(a.count(1))  # 1 在 元组 a 中出现的次数
# len() 函数可以统计元素的个数
print(len(a))  # 元组的元素个数
# max() 函数可以返回元组中元素最大值
print(max(a))  # 元组 a 中元素的最大值
# min() 函数可以返回元组中元素最小值
print(min(a))  # 元组 a 中元素的最小值
