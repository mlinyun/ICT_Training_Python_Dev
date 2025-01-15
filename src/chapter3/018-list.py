# 列表

# 列表可以包含不同类型的元素，但一般情况下，会在其中存储类型相同的元素
# 列表是可变数据类型
a = [1, 2, 3]
print(a)
print(type(a), id(a))
a.append(4)
print(type(a), id(a))
# 通过列表的内置方法给列表新增了一个元素，但 id 值仍然保持不变

"""列表的创建"""
# 使用一对方括号来表示空列表: []
a = []
print(a)
print(type(a))
# 使用方括号，其中的项以逗号分隔: [a] 或 [a, b, c]
a = [1]
print(a)
print(type(a))
b = ["a", "b", "c", "d"]
print(b)
print(b)
# 使用列表推导式: [x for x in iterable]，iterable 是可迭代对象
t = (1, 2, 3, 4, 5, 6)
a = [i * 2 for i in t]
print(a)
string = "abcdefg"
a = [i + "-" for i in string]
print(a)
# 使用类型的构造器: list() 或 list(iterable)
a = list()  # 创建一个空列表，与 a = [] 一样
print(a)
print(type(a))
n = "abcdefg"
b = list(n)  # 将字符串转换为列表
print(b)
print(type(b))

"""列表的索引和切片"""
# 和字符串、元组一样，列表也支持索引和切片
s = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(s[0])  # 获取索引 0 处的元素
print(s[-1])  # 获取索引 -1 处的元素
print(s[0:3])  # 切片
print(s[::-1])  # 翻转
print(s[::-2])  # 步长为 2 生成新列表

"""列表元素的添加"""
# append() 方法可以在列表末尾追加元素
a = [1, 2, 3]
print(a)
a.append(4)  # 末尾追加元素 4
print(a)
# extend() 方法可以通过可迭代对象将多个元素到列表中
a = [1, 2, 3, 4, 5]
print(a)
a.extend("abcde")  # 把字符串的每个字符添加到列表中
print(a)
a.extend([6, 7, 8, 9, 10])  # 通过列表添加多个元素到列表 a
print(a)
# insert() 方法可以按照索引插入元素
t = ["a", "c", "d", "e"]
print(t)
t.insert(1, "b")  # 在索引 1 的位置插入元素 "b"
print(t)

"""列表元素的删除"""
# pop() 方法是列表的内置方法，有个可选参数索引（ index ）默认是 -1
# 也就是说默认删除最后一个元素，我们也可以设定需要删除的元素索引
# pop() 方法在删除元素后会返回删除的元素
letters = ["a", "b", "c", "d", "e", "f", "g"]
print(letters)
letters.pop()  # 默认删除最后一个元素
print(letters)
letters.pop(3)  # 指定索引，删除第 4 个元素
print(letters)
# remove() 方法是根据元素的值进行删除，所以必须指定要删除的元素
# remove() 方法删除之后不会返回删除的元素，这一点与 pop() 方法不同
a = [1, 2, 3, 4, "5", 6, 7, "8", 9]
print(a)
a.remove(2)  # 删除元素 2
print(a)
a.remove("8")  # 删除元素 "8"
print(a)
# clear() 方法会清空列表
a = [1, 2, 3, 4, "5", 6, 7, "8", 9]
a.clear()
print(a)
# del 语句
# del 语句和 pop() 方法一样，也是使用索引进行删除元素
# 不过 del 语句不会返回删除的元素。 del 语句还可以删除切片
# 甚至删除整个列表，这一点 pop() 方法就不支持
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
del a[-1]  # 删除最后一个元素
print(a)
del a[2:5]  # 删除切片[2:5]
print(a)
del a[:]  # 删除列表中全部元素
print(a)
del a  # 删除列表
# print(a)

"""列表的修改"""
# 列表可以通过索引或切片赋值改变列表元素，甚至清空整个列表
letters = ["a", "b", "c", "d", "e", "f", "g"]
print(letters)
letters[0] = "A"  # 通过索引将第一个元素修改为 "A"
print(letters)
letters[2:5] = ["C", "D", "E"]  # 通过切片对第 3、4、5 个元素进行修改
print(letters)
letters[5:] = []  # 将第 6 个之后的元素清空
print(letters)
letters[:] = []  # 将整个列表清空
print(letters)
# 列表排序
# 内置方法 sort 可以实现对列表的排序
letters = ["a", "aa", "B", "cc", "b", "A", "bb", "c"]
letters.sort()  # 默认按照 Unicode 数值排序，数值越小越靠前
print(letters)
# 可选参数 reverse 默认 Flase ，如果设置为 True 就是反向排序
letters.sort(reverse=True)
print(letters)
# 另外还有一个可选参数 key 可以实现更复杂的排序
letters = ["a", "aa", "B", "cc", "b", "A", "bb", "c"]
letters.sort(key=str.upper)  # 按照大写字母的形式排序
print(letters)
letters.sort(key=str.lower)  # 按照小写字母的形式排序
print(letters)
letters.sort(key=len)  # 按照元素的长度排序，元素必须是可迭代对象
print(letters)
# reverse() 方法可以实现对列表 x 的翻转，与切片 x[::-1] 类似
# 不过切片不会修改原列表，所以更推荐使用切片
letters = ["a", "aa", "B", "cc", "b", "A", "bb", "c"]
print(letters)
new_letters = letters[::-1]  # 翻转之后的结果，如果有需要，可以赋值给其他变量
print(letters)  # 原列表没有改变
letters.reverse()
print(letters)  # 原列表已改变

"""列表的查询"""
# 通过内置方法 count() 查看元素出现的次数
fruits = ["orange", "apple", "pear", "banana", "kiwi", "apple", "banana"]
print(fruits.count("apple"))
print(fruits.count("tangerine"))
# 通过内置方法 index() 返回列表中第一个值为 x 的元素的索引值
# 未找到指定元素时，触发 ValueError 异常。可选参数 start 和
# end 是切片符号，用于将搜索限制为列表的特定子序列
# 但返回的索引仍然是基于整个序列计算的
fruits = ["orange", "apple", "pear", "banana", "kiwi", "apple", "banana"]
print(fruits.index("banana"))
print(fruits.index("banana", 4))  # 从第 5 个元素开始寻找

"""列表嵌套"""
# 嵌套列表就是在列表中包含列表
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(a[0])
print(a[0][0])

"""列表的运算符"""
# 列表和字符串、元组一样，也是支持很多运算符
print([1, 2, 3] + [4, 5])  # + 运算符实现列表合并
print([1, 2, 3] * 3)  # * 运算符实现重复
print(3 in [1, 2, 3])  # in 运算符判断字符是否在列表中
print(3 not in [1, 2, 3])  # not in 运算符
