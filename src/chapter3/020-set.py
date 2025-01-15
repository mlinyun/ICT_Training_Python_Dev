# 集合

# 集合（set）是一个无序的不重复元素序列
# 满足数学上集合的三大属性 确定性、互异性、无序性
# 集合是可变数据类型，可以通过下面的代码进行验证
letters = {"a", "b", "c"}
print(letters)
print(type(letters), id(letters))
letters.add("d")  # 增加一个元素 "d"
print(letters)
print(type(letters), id(letters))
# 可以看到，我们通过内置方法给集合新增了一个元素，
# 但内存地址没有发生改变，证明了集合是可变数据类型

"""集合的创建"""
# 使用花括号内以逗号分隔元素的方式
a = {"jack", "sjoerd"}
print(a)
print(type(a))
# 使用集合推导式
string = "abracadabra"
a = {i for i in string}  # 集合在创建时会自动去掉重复元素
print(a)
print(type(a))
# 使用类型构造器 set() 创建集合
a = set()  # 可以创建空集合，不能用 {} 创建
print(a)
print(type(a))
b = {}  # 这样创建的是字典
print(b)
print(type(b))
c = set("foobar")  # 通过可迭代对象创建集合，会自动去重
print(c)
print(type(c))

"""集合添加元素"""
# 使用 add() 方法新增元素
letters = {"a", "b", "c"}
print(letters)
letters.add("d")  # 新增一个元素 "d"
print(letters)
# 使用 update() 方法可以将可迭代对象中的元素添加到集合中
letters = {"a", "b", "c"}
print(letters)
letters.update("defg")  # 从字符串中添加
print(letters)
letters.update(["h", "i", "j", "k"])  # 从列表中添加
print(letters)

"""集合删除元素"""
# 集合的无序性，所以它不存在切片索引的功能
# remove() 方法会删除指定的元素，如果元素不存在就会报错
letters = {"a", "b", "c"}
letters.remove("a")  # 删除元素 "a"
print(letters)
# letters.remove("d")  # 元素不存在会报错
# discard() 方法和 remove() 方法类似，不过当遇到不存在的元素时不会报错
letters = {"a", "b", "c"}
letters.discard("a")  # 删除元素 "a"
print(letters)
letters.discard("d")  # 元素不存在不会报错
print(letters)
# pop() 方法会随机删除元素
letters = {"a", "b", "c", "d", "e", "f"}
print(letters)
letters.pop()  # 随机删除元素
print(letters)
# clear() 方法会清空全部元素
letters = {"a", "b", "c", "d", "e", "f"}
print(letters)
letters.clear()  # 清空元素
print(letters)
# del 语句可以删除整个集合
letters = {"a", "b", "c", "d", "e", "f"}
del letters
# print(letters)  # 报错

"""集合的运算"""
# 交集：交集是两个集合的公有部分
# intersection 方法
a = {"a", "r", "b", "c", "d"}
b = {"a", "l", "c", "m", "z"}
print(a.intersection(b))
# & 运算符
print(a & b)
# 并集：并集是合并两个集合
# union() 方法
print(a.union(b))
# | 运算符
print(a | b)  # 需要注意的是，求并集使用 | 运算符，不能使用 +
# 差集：两个集合 A 和 B，所有属于 A 且不属于 B 的元素构成的集合
# 称为 A 与 B 的差集（A - B）。根据概念，我们知道两个求差集是
# 有先后顺序的，A 与 B 的差集 和 B 与 A 的差集 就属于两回事
# difference() 方法
print(a.difference(b))  # a 与 b 的差集
print(b.difference(a))  # b 与 a 的差集
# - 运算符
print(a - b)  # a 与 b 的差集
print(b - a)  # b 与 a 的差集R

"""列表去重"""
# 集合具有互异性，通俗来说就是唯一性，不会出现重复的元素
# 所以我们就可以使用集合给列表去重
a = [1, 2, 3, 2, 5, 3, 2, 1]
b = set(a)  # 将列表转换为集合
c = list(b)  # 将集合转换回列表
print(c)
