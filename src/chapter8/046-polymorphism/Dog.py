import Animal


class Dog(Animal.Animal):  # 继承 Animal 类
    def __init__(self, name, age):
        # super 方法的固定用法，它的作用是运行父类的同名方法
        # 如果父类的同名方法有十行，这里的一行就可以代替了
        # 注意参数不需要写 self
        super().__init__(name)
        # 上面这一行等同于 Animal.Animal.__init__(self, name)
        self._age = age

    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age

    # 子类重写父类的 say 方法，该方法用来打印狗的叫声
    def say(self):
        print(f"{self._name} is making sound wang wang wang...")
