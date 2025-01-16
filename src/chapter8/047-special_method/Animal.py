class Animal:
    # 设置该类的实例只能定义名字、年龄两个属性
    __slots__ = ("_name", "_age")

    # 需要注意的是：__slots__ 的作用只在定义的类中有效，在继承该类的子类中是无效的
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value

    def say(self):
        print(self._name + 'is saying something')
