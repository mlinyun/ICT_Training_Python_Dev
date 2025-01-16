# 函数定义
def hello():
    print('Hello World!')


# 函数调用
hello()


# 形参和实参
def hello(name):
    print(f'Hello {name}!')


hello('John')
hello('张三')
hello('李四')


# 默认值参数
def hello(name="World!!!"):
    print(f'Hello {name}!')


hello()
hello("Jobs")


# 关键字参数
def person(name, age):
    print(f"{name}今年{age}岁了。")


person(name="张三", age=25)
person(age=50, name="李四")


# 可变参数
# 定义可变参数的方法其中一种是在参数名前面加上星号 *
# 该参数会以元组(tuple)的形式导入，存放所有未命名的变量参数
def total(first, *number):
    print(type(number))
    print(number)
    print(sum(number, first))


total(1)
total(1, 2)
total(1, 2, 3, 4)


# 另外一种定义可变参数的方法是在参数前加上两个星号 **
# 该参数会以字典（dict）的形式接收关键字形式的引用
def person(name, age, **other):
    print(f'姓名：{name}')
    print(f'年龄：{age}')
    print(f'其他信息：{other}')


person('王五', 26, gender="男", job="作家")
person('赵六', 28, gender='女', job="画家", city="北京")


# 特殊参数
# 默认情况下，参数可以按位置或关键字传递给函数
# 但有时候为了让代码易读、高效，我们会限制参数的传递方式，如仅按位置
# 传递参数、仅按关键字传递参数、同时包含仅按位置参数和仅按关键字参数
# 仅按位置传递参数
# 仅按位置传递参数的函数，其形参应该放在斜杠（/）前面
def school(name, city, /):
    print(f"学校名称：{name}")
    print(f"所在城市：{city}")


school("浙江大学", "杭州")
# school(name="北京大学", city="北京") # 报错


# 仅按关键字传递参数
# 仅按关键字传递参数的函数，形参应该放在星号（*）后面
def school(*, name, city):
    print(f"学校名称：{name}")
    print(f"所在城市：{city}")


# school("浙江大学", "杭州") # 报错
school(name="北京大学", city="北京")


# 同时包含仅按位置参数和仅按关键字参数
def school(name, /, shortname, *, city):
    print(f'学校名称：{name}')
    print(f'学校简称：{shortname}')
    print(f'所在城市：{city}')


school("北京大学", "北大", city="北京")
school("北京大学", shortname="北大", city="北京")
# 斜杠前面只能是位置参数，星号后面只能是关键字参数
# 中间地带正好是两不管，也就是一般的参数，你可以自由选择任意方式调用
