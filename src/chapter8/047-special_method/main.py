import Bird
import Book
import Dog

# 类中的特殊方法
# __new__() 方法 创建实例的方法
# 目标：在实例化 Dog 类的时候打印一行信息: "A new dog."
dog = Dog.Dog("Tom", 11)  # 终端会打印 "A new dog."

# __del__() 方法 销毁实例的方法
dog.__del__()  # 对象可以直接调用 __del__ 方法，但并不会删除自己
print(dog)
del dog  # 如果对象有 __del__ 方法，del 语句执行时会顺便执行该方法
# print(dog)  # 报错

# __slots__ 属性 限制绑定属性类别
# 在 Python 中，定义一个实例对象后是可以绑定任意的属性
bird = Bird.Bird("Tony")
bird._age = 4  # 类未定义，继承了父类
bird.hometown = 'New York'  # 子类定义的
# bird.role = 'bird'  # 子类父类的 __slots__ 方法均没有，所以报错

# __call__() 方法
# 在 Python 中一切皆对象，对象分为可调用的和不可调用的
# 凡是可以通过一对括号 () 来调用的都是可调用对象，比如函数、类等
# 我们可以通过 Python 的内置 callable 函数来判断一个对象是否是可调用对象
print(callable(Dog))  # 类是可调用对象
print(callable(bird))  # 类的实例是不可调用对象
def hello():
    print('Hello World!')
print(callable(hello))  # 函数是可调用对象
# 当我们在类中定义 __call__ 方法，这样类的实例就是可调用对象了
book = Book.Book("西游记")
book()  # Book 类中定义了 __call__ 方法，故其实例是可调用对象
print(callable(book))
