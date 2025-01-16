# 类和对象

"""类的定义"""
# 创建类的关键字是 class
class Cat:  # 类 = 属性 + 方法
    # 属性
    age = 1
    role = "cat"

    # 方法
    def call(self):
        print(f"miao~ miao~ miao~")


# 创建实例 xiaohua
xiaohua = Cat()
print(xiaohua.age)
print(xiaohua.role)
xiaohua.call()

# 查看实例的属性和方法
print(dir(xiaohua))

"""类的构造方法 __init__"""


class A:
    # 构造方法
    def __init__(self):
        self.data = ["A"]


a = A()
data = a.data
print(data)


"""自定义打印样式 __repr__"""
class Cat2:
    # 构造方法
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 自定义方法
    def call(self):
        print(f"miao~ miao~ miao~")

    # 自定义打印样式
    def __repr__(self):
        return f"Cat: {self.name} {self.age}"


xiaohua2 = Cat2("xiaohua2", 2)
print(xiaohua2.name)
print(xiaohua2.age)
xiaohua2.call()
print(xiaohua2)
