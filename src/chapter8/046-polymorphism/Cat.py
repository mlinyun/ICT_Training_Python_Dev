import Animal


class Cat(Animal.Animal):  # 继承 Animal 类
    def __init__(self, name, age):
        super().__init__(name)
        self._age = age

    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age

    # 子类重写父类的 say 方法，该方法用来打印猫的叫声
    def say(self):
        print(f"{self._name} is making sound miao miao miao...")
