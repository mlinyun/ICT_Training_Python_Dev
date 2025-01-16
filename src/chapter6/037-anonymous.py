# 匿名函数
double = lambda x: x * 2
# Lambda 函数可用于任何需要函数对象的地方
# 在语法上，匿名函数可以有多个参数，但只能有一个表达式
num = double(10)
print(num)

# 很多时候，我们会把匿名函数作为其他函数的实参来使用
# 比如内置函数 sorted() 有一个可选的参数 key，用于配置排序的方式
# 目标：使用每个元素最后一位进行排序
# 使用一般函数，代码如下：
a = ["dog", "abandon", "cool", "black"]
def select(x):
    return x[-1]
b = sorted(a, key=select)
print(b)
# 改用 lambda 函数实现
c = sorted(a, key=lambda x: x[-1])
print(c)
# 可以看到，lambda 函数更加简洁。一般函数可能需要好几行才能实现的功能，lambda 函数一行就搞定了


"""lambda 函数的其他示例"""
# lambda 函数的参数是可选的
a = lambda: True
print(a())  # True
# lambda 函数可以使用多个参数
add = lambda x, y: x + y
print(add(2, 3))  # 5
# lambda 函数可以设置参数默认值
a = lambda x=5: x ** 2
print(a())  # 5^2 = 25
print(a(4))  # 4^2 = 16
# lambda 函数可以配合括号直接使用
num = (lambda x=5: x ** 2)(3)  # 3^2 = 9
print(num)
