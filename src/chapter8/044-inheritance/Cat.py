import Animal


class Cat(Animal.Animal):  # 继承 Animal 类
    # 该方法用来打印猫的叫声
    def say(self):
        print(f"{self._name} is making sound miao miao miao...")
