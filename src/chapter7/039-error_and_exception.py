# 异常和错误

# Python 中所有错误异常类都继承自 Exception

exception = [i for i in dir(__builtins__) if "Error" in i]
print(exception)

# 我们可以通过特殊方法 __doc__ 查看对应的异常类帮助文档
print(TabError.__doc__)  # TabError 是指空格和 Tab 键的混合输入

"""语法错误"""
# 缩进错误
# for i in range(10):
#     if i < 5:
#         print(i)
# 	else:
#         print("no")
# 上面的这段代码看起来没有问题，但是因为空格和 Tab 键进行混用，导致发生错误
# 缩进推荐使用 4 个空格，并且要避免将空格和 Tab 键混用

# 全角标点符号
# Python 语法中使用的标点符号都必须是英文半角符号
# print（"hello"）

# 单双引号混用
# print("hello")

# 循环语句缺少冒号
# for i in range(10)
#     print(i)


"""常见异常"""
# 逻辑错误
# 逻辑错误是指语法可能没问题，但不符合逻辑
# 比如我们都知道数学上除数不能为 0
# 当你在 Python 中将除数设置为 0 ，就会出现错误
# print(5 / 0)

# 命名错误（NameError）
# 命名错误一般是指拼写错误，这是个非常常见的错误
# for i in rnage(10):
#     print(i)

# 类型错误 （TypeError）
# print("鲁迅生于" + 1881 + "年")

# 索引错误（IndexError）
# a = [1, 2, 3]
# print(a[8])

# 值错误（ValueError）
# print(int("happy"))
