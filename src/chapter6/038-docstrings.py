# 文档字符串

# 查看内置函数 print() 的文档
# print(help(print))
print(print.__doc__)
print()
# 查看 str() 函数的帮助文档
print(str.__doc__)
print()


# 文档字符串的使用
def hello(name, greet="Hello"):
    """
hello(name)
hello(name,greet="Hello")
这是一个问好的程序，参数 name 表示问好的对象，
可选参数 greet 是问好的方式，默认是 Hello
    """
    print(f"{greet} {name}")


print(hello.__doc__)
