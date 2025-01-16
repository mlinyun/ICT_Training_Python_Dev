import Animal


class Dog(Animal.Animal):
    # 如果在子类中也定义此属性，则该属性会继承父类的同名属性，也就是说
    # 子类的实例可以定义的属性为子类和父类的 __slots__ 属性值之和
    __slots__ = ("hometown")

    # 注意此方法的第一个参数为 cls ，指向类本身
    # 在 __init__ 方法中用到的参数须写入，self 除外
    def __new__(cls, name, age):
        print("A new dog.")
        # 使用 super 方法调用父类的同名方法
        return super().__new__(cls)
        # 下面这一行的作用与上一行等效，都是将 “调用父类方法” 作为返回值
        # return object.__new__(cls)

    # 初始化实例方法（构造方法）
    def __init__(self, name, age):
        super().__init__(name)
        self._age = age

    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age

    # 子类重写父类的 say 方法，该方法用来打印狗的叫声
    def say(self):
        print(f"{self._name} is making sound wang wang wang...")

    # 销毁实例的方法
    def __del__(self):
        print(f'删除了 {self._name} 实例')
