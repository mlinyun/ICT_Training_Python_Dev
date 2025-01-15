# 字典

# 字典（dict） 也是一种常用的 Python 內置数据类型
# 前面我们学习过的字符串、元组、列表都是使用从 0 开始的整数作为索引
# 而字典以键（key）为索引，键通常是字符串或数字，也可以是其他任意不可变类型
# 字典中每一个 元素 都是一个 key 和一个 value 的组合
# 我们可以把字典理解为 键值对 的集合，字典的键必须是唯一的
# 字典是可变数据类型

age = {'James': 23, 'Leonard': 25, 'Antetokounmpo': 32, 'Durant': 24}  # 这是一个字典
print(age)
print(type(age), id(age))
age['Harden'] = 19  # 字典增加元素
print(age)
print(type(age), id(age))

"""字典的创建"""
# 在花括号（{}）内以逗号分隔 键:值 对的方式
a = {}  # 创建空字典
print(a)
print(type(a))
b = {"jack": 4098, "sjoerd": 4217}
print(b)
print(type(b))
# 使用字典推导式
a = {x: x ** 2 for x in range(10)}
print(a)
# 使用类型构造器 dict() 创建字典
s = dict()  # 创建空字典
print(s)
print(type(s))
a = {"one": 1, "two": 2, "three": 3}
b = dict(one=1, two=2, three=3)
c = dict([("one", 1), ("two", 2), ("three", 3)])
d = dict({"one": 1, "three": 3, "two": 2})
e = dict({"one": 1, "three": 3}, two=2)
print(a == b == c == d == e)  # a、b、c、d、e 都一样
print(b)
print(type(b))

"""字典的查询"""
# 可以通过 d[key] 的方式查询字典 d 中以 key 为键的项的值
a = {"one": 1, "two": 2, "three": 3}
print(a["one"], a["three"])
# print(a["four"])  # 报错
# 基于上面的原因，我们更推荐使用字典的内置方法 get()
# 该方法在查询时遇到不存在的 key 不会报错，而是会默认
# 返回 None，我们也可以自行定制返回值
print(a.get("one"))  # key 存在则返回其对应的值
print(a.get("four"))  # key 不存在不会报错，而是返回 None
print(a.get("four", "这个值不存在！"))  # 自定义 key 不存在时返回的值

"""字典元素的增加和修改"""
"""
在字典中 增加元素 和 修改元素 的代码其实是相同的，只需要为字典中某一个 key 进行赋值，区别在于：
    - 如果此时 key 存在，则判断为你在修改元素，更新该 key 对应的 value 值
    - 如果不存在，则判断为你在添加元素，向字典中增加该 key: value 键值对，
      从 Python 3.6 开始，Python 会保持元素插入顺序，新的元素会在字典末尾
"""
a = {"one": 1, "two": 2, "three": 3}
a["one"] = "一"  # 修改元素
print(a)
a["four"] = 4  # 添加元素
print(a)

"""字典的删除"""
# pop(key[, default]) 方法在 key 存在于字典时会删除并返回对应的值（value）
# key 不存在时返回 default，没有设置 default 会发生 KeyError 异常
a = {"one": 1, "two": 2, "three": 3}
a.pop("one")  # 删除后会返回 "one" 对应的值
print(a)
a.pop("four", "您正在删除不存在的内容")  # 设置 default
# a.pop("four") # 未设置 default，当删除不存在的值会报错

# popitem() 方法会从字典中删除并返回一个 (键, 值) 元组
# 因为从 Python 3.6 开始，dict 对象会保持插入时的顺序
# 所以该方法保持后进先出的删除顺序，当字典为空时会发生 KeyError 异常
a = {"one": 1, "two": 2, "three": 3}
print(a.popitem())
print(a.popitem())
print(a.popitem())

# del 语句需要指定 字典名 和需要删除的 key 值，key 不存在时发生 KeyError 异常
a = {"one": 1, "two": 2, "three": 3}
del a["one"]
print(a)
# del a["four"] # 删除不存在的内容会报错


# clear() 清空字典
a = {"one": 1, "two": 2, "three": 3}
a.clear()  # 清空字典
print(a)

"""字典视图对象"""
# 由 dict.keys(), dict.values() 和 dict.items() 所返回的对象称为视图对象
a = {"one": 1, "two": 2, "three": 3}
print(a.values())  # 由字典的键（key）组成
print(a.keys())  # 由字典的值（value）组成
print(a.items())  # 由字典项 ((键, 值) 对) 组成
# 字典视图对象是可迭代的，所以可以通过 list()、set()、tuple() 等构造函数
# 将其转换成对应的类型，然后就可以进行切片索引之类的操作
keys = a.keys()
print(list(keys))  # 转换成列表 list
print(set(keys))  # 转换成集合set
print(tuple(keys))  # 转换成元组 tuple
