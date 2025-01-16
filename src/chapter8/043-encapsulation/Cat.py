# 此类是猫的集合，此类的实例是具体的某一只猫
class Cat:
    def __init__(self, name):
        # Python 的私有属性用一个或两个下划线开头表示
        # 一个下划线开头的私有属性表示外部调用者不应该直接调用，但还是可以调用
        # 两个下划线外部就不能直接调用了，但也有办法
        self._name = name

    # 私有属性 _name 不可以被直接调用
    # 因此需要定义两个方法来修改和获取该属性值
    # get_name 用来获取属性值
    def get_name(self):
        return self._name

    # set_name 用来修改属性值
    def set_name(self, name):
        self._name = name

    # 该方法用来打印猫的叫声
    def say(self):
        # 这里 self._name 就是直接调用私有属性
        # 在类的内部可以这样写，在类的外部不可以哦
        print(f"{self._name} is making sound miao miao miao...")
