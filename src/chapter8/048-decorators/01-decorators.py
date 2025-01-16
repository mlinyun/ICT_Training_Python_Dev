# 认识装饰器
from functools import wraps
from datetime import datetime


# Python 内置的 datetime 类可以实现打印当前日期和时间
# print(datetime.now())


# 目标：让函数每次运行都会先打印运行的时间
# def hello(name):
#     print(datetime.now())
#     print(f"Hello, {name}")


# hello("Tom")
# 只要我们在函数内增加上面打印时间的语句，就能够实现上面的目标
# 但是如果我们有很多个函数都想增加这样的功能，一个个去修改就有点麻烦
# 而使用装饰器就可以在不修改原有函数的情况下实现这样的功能
def hello(name):
    print(f"Hello, {name}")


def print_datetime(func):
    def wrapper(*args, **kw):
        print(datetime.now())
        func(*args, **kw)

    return wrapper


f = print_datetime(hello)
f("Tom")


# 上面的例子中，print_datetime 是一个装饰器，我们以 hello 函数作为参数
# 运行后返回值为 wrapper，也是一个函数。然后调用 wrapper 函数，调用函数
# 的方式就是在函数名后面加上括号。该函数的参数会传递给内部的 func 函数，
# 也就是我们传入的 hello 函数


# Python 还支持一种更简短的方式生成一个被装饰器修饰的函数，就是使用 @ 符号
@print_datetime
def hello2(name):
    print(f"Hello2, {name}")


hello2("Tom2")
print(hello2.__name__)


# 此时定义的函数 hello 就是一个被装饰器 print_datetime 修饰的函数
# 虽然名字是 hello，但实际上是 print_datetime 函数的返回值 wrapper 函数
# 我们通过特殊属性 __name__ 也进行了验证


# 那么如何让使用了装饰器的 hello 函数仍然是它本身，而不是 wrapper 呢？
# 可以使用 functools 模块中的 wraps 装饰器。functools 模块是函数的
# 工具模块，里面有很多实用的工具，wraps 就是其中之一
def print_datetime2(func):
    @wraps(func)
    def wrapper(*args, **kw):
        print(datetime.now())
        func(*args, **kw)

    return wrapper


@print_datetime2
def hello3(name):
    print(f"Hello3, {name}")


hello2("Tom3")
print(hello3.__name__)
