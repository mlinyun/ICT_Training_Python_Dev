"""字符串"""
string = "hello"
print(id(string), type(string))
string = "world"
print(id(string), type(string))
# 当 string 的值发生了改变，它的内存地址也就会相应的发生变化，所以字符串是不可变数据类型

"""字符串索引"""
string = "abcdef"
print(string[0], string[1], string[2])  # 正索引
print(string[-1], string[-2], string[-3])  # 负索引
# 因为字符串是不可变数据类型，如果给某个索引位置赋值就会报错
# string[0] = "A"

"""字符串切片"""
string = "0123456"
# 切片语法 string[start:end:step]
str_01 = string[0:2]  # 返回索引 0，1 位置的字符
print(str_01)
str_35 = string[3:6]  # 返回索引 3，4，5 位置的字符
print(str_35)
str__2 = string[:3]  # start 参数默认为 0，返回索引 0，1，2 位置的字符
print(str__2)
str_1_ = string[4:]  # end 参数默认到行尾(包含行尾)，返回索引 4，5，6 位置的字符
print(str_1_)
str___ = string[:]  # start 0，end 默认行尾，返回整个字符串
print(str___)
str_45 = string[-3:-1]  # 也可以使用负索引，返回索引为 -3，-2 位置的字符
print(str_45)
# 切片中第三个参数为步长
# 步长可以是正数，也可以是负数，但不能为 0
# 当步长为负数时，start 的默认值是行尾，end 默认值是 0
# 但 start 和 end 依旧满足 “包头（start）不包尾（end）”
string = "0123456789"
str_0369 = string[0:10:3]
print(str_0369)
str_9630 = string[::-3]
print(str_9630)
# 将字符串进行翻转
str_re = string[::-1]
print(str_re)
# 切片会自动处理索引 end 的越界问题
print(string[8:100])
print(string[-8:-100:-1])

"""转义字符"""
# 续行符 \
print("Hello, \
    world!")

# 引号 \' 和 \"
# print('It's OK！')
print('It\'s OK！')

# 响铃 \a
print("\a")

# 退格(Backspace) \b
# 退格符会将光标退回前一个字符，不会删除光标后面的字符
# 但当退格符后边有新的字符时，将会覆盖退回的那个字符
print('hello  \bworld !')  # 此处会退格后继续书写
print('hello world !\b')  # 此处退格符后面没有内容，所以没有变化。

# 换行符 (\n) 光标到下一行
print("Hello World!\nHello World!")

# 回车 (\r) 光标重新回到本行开头
print("Hello\rWorld!")

# 横向制表符 \t
print("Hello\tWorld!")

# 纵向制表符 \v
print("Hello\vWorld!")

# 八进制: 1~3位八进制数据所表示的 ASCII 字符
print("\110\145\154\154\157\40\127\157\162\154\144\41")

# 十六进制: 4位十六进制数据所表示的字符
print("\x48\x65\x6c\x6c\x6f\x20\x57\x6f\x72\x6c\x64\x21")

# 避免转义 \
# 当我们遇到上述特殊字符但不需要转义时，我们可以在特殊字符前面加上反斜杠 \ 避免转义
print("D:\tt\no\reseach")  # 默认输出的效果
print("D:\\tt\\no\\reseach")  # 避免转义之后
# 可以看到，默认输出的结果简直面目全非，而加上反斜杠 \ 避免转义之后，输出了我们想要的结果

"""字符串运算符"""
# in 操作符: 如果字符串包含指定字符就返回 True，否则返回 False
print("e" in "hello", "f" in "hello")
# not in 操作符: 如果字符串不包含指定字符就返回 True，否则返回 False
print("e" not in "hello", "f" not in "hello")
# 字符串拼接 (+) 字符串可以使用 + 将两段字符串进行拼接
message = "明天是" + "周六"
print(message)
# 重复运算符 (*)
print("=" * 5 + "测试" + "=" * 5)
# 原始字符串 (r)
# 原始字符串，是在引号前面加上 r 或 R，这样遇到特殊字符就不会转义，而是普通输出
print("C:\Windwos\no\reseach")  # 默认输出的效果
print(r"C:\Windwos\no\reseach")  # 原始字符串效果

"""字符串格式化"""
# 使用 + 运算符实现对字符串的拼接时；如果想把数字和字符串拼接在一起
# 会报错，可以使用 str() 函数将数字转换为字符串格式
# message = "今年是" + 2025 + "年" # 报错
message = "今年是" + str(2025) + "年"
print(message)

"""f-string 格式化"""
year = 2021
month = 4
day = 1
print(f"今天是{year}年{month}月{day}日")
# 格式说明符 写在冒号（:）后面
pi = 3.1415926
# .2f 是指小数点后两位小数，f 是定点表示法
# 在没有指定精度时，会对浮点数采用小数点后 6 位有效数位的精度
print(f"圆周率保留两位小数是：{pi:.2f}")  # 指定精度
print(f"圆周率保留两位小数是：{pi:f}")  # 未指定精度
# 设置字段最小字符宽度，常用于列对齐
print(f"字符宽度设置为6，并保留2位小数：{pi:6.2f}")
name1 = 'Bob'
age1 = 20
name2 = 'John'
age2 = 25
print(f"{name1:6}=>{age1:6}\n{name2:6}=>{age2:6}")
# 如果是数字，还可以指定用 0 填充，就会在数字前面加 0
total = 1234
print(f"金额总数：{total:08} 元")
# 千位分隔符 数字还可以使用 _ 或者 , 作为千位分隔符，让数字的阅读更加方便
print(f"{100000000000}")
print(f"{100000000000:_}")
print(f"{100000000000:,}")
# _b, _o, _x 可以让二进制、八进制、十六进制每隔 4 个数码进行分隔
print(f"{0b10000000:_b}")  # 二进制分隔表示
print(f"{128:_b}")  # 十进制数会先转二进制，然后分隔
print(f"{10000:_o}")  # 十进制数转八进制，然后分隔表示
print(f"{12800000:_x}")  # 十进制数会先转十六进制，然后分隔表示
# 百分比 可以使用 % 将数字转换为百分比形式。和 f 转换一样，不指定精度会按小数点后 6 位精度
print(f"{0.25:%}")  # 不指定精度
print(f"{0.25:.2%}")  # 指定精度
# 其他修饰符 还有一些修饰符可以在格式化前转换值
# !a 对应 ascii() 函数，!s 对应 str() 函数，!r 对应 repr() 函数
name = '苏轼'
print(f'{name!a}')
print(f'{name!s}')
print(f'{name!r}')
# 时间类型格式化
import datetime

date = datetime.datetime(2025, 1, 15, 5, 20, 0)
print("{:%Y-%m-%d %H:%M:%S}".format(date))

"""format 格式化"""
# 位置引用 format 格式化是将传递给 format 方法的对象传递到花括号内
print('We are the {} who say "{}!"'.format('knights', 'Ni'))
# 还可以在花括号中加上的数字表示传递给 str.format() 方法的对象所在的位置
print('{0} and {1}'.format('spam', 'eggs'))
print('{1} and {0}'.format('spam', 'eggs'))
# 关键字引用
print('他今年 {age} 岁，在{city}工作。'.format(age=25, city='北京'))
# 对于字符或者数字的格式限定和上面的 f-string 基本类似
# 只是需要将需要引用的值放到 format() 方法内。需要注意的是 format() 方法不支持表达式
pi = 3.1415926
print("圆周率是：{:6.2f}".format(pi))

"""% 格式化"""
# % 运算符也可用于字符串格式化，不过因为有很多怪异特性，导致很多错误，官方已经不推荐使用
print("%s %s" % ("Hello", "World"))
print("圆周率是：%6.2f" % pi)

"""三引号"""
# 使用三引号的字符串可以跨越多行，而且可以将所有的空白字符都包含在该字符串中
# 如果有保持样式的需求，那么就需要使用三引号
print('''\
===========字符串===========

三引号字符串会保留空白字符，
从而实现保持样式的效果
''')

"""字符串方法"""
# 字符串对象有很多内建方法，我们通常会使用 dir() 函数查看
# dir() 函数会列出该对象的属性和方法
a = " Hello, World! "
print(dir(a))
# 当我们想知道某个方法的使用方法，我们会使用 help 函数查看
# print(help(a.upper))

# upper() 方法返回大写的字符串
print(a.upper())
# lower() 返回小写的字符串
print(a.lower())
# swapcase() 返回字符串大小写交换后的版本
print(a.swapcase())
# replace(old,new) 对字符串中的子字符串进行替换
print(a.replace("World", "Langqiao"))
# strip() 方法默认会删除开头和结尾的空白字符
print(a.strip())
# 也可以指定开头和结尾的其他字符
b = "==============Hello, World!=============="
print(b.strip("="))
# split() 方法默认以空格作为分隔符对字符串进行拆分
# 连在一起的空格会被视为单个字符，分隔之后会以列表形式返回
print(a.split())
# 指定分隔符进行拆分
print(a.split(","))
# join() 方法可以使用指定字符串连接多个字符串
print("-".join(a.split()))
# find() 方法可以返回要查找的子字符串的最小索引
print(a.find("Wo"))
# len() 函数 通过 Python 的内置函数 len() 获得字符串的长度
print(len(a))
