# 函数的返回值
def hello():
    return 'Hello World!'


a = hello()
print(a)


# 变量作用域
# Python 中有两种基本的变量作用域：局部变量 和 全局变量
# 局部变量
# 在函数内部定义的变量名只能被函数内部引用，不能在函数外引用
# 这个变量的作用域就是局部的，所以它就是一个局部变量
def person():
    age = 20
    print(f'从函数内部访问变量 age 的值：{age}')


person()
# print(f'从函数外面访问变量 age 的值：{age}') # 报错


# 函数内部只作引用的 Python 变量会被隐式的视为全局变量
a1 = 5
def x():
    print(a1)


x()

# 如果在函数内部任何位置为变量赋值，除非明确声明为全局变量，否则均将其视为局部变量
a2 = 8
def x():
    # a2 += 1 # 此时函数内部的 a2 属于局部变量，当尝试改变它的值时，就会报错
    print(a2)


x()

# 要想声明全局变量，我们就需要使用 global 关键字
a3 = 8
def x():
    global a3
    a3 += 1
    print(a3)


x()
print(a3)


# nonlocal 变量
# 还有一个 nonlocal 关键字，但它只用在嵌套函数内部
# 嵌套函数就是函数内部的函数
def outer():
    num = 1

    def inner():
        nonlocal num  # nonlocal关键字声明
        num = 2
        print(num)

    inner()
    print(num)


outer()
