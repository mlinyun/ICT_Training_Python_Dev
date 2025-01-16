import Animal


class Dog(Animal.Animal):  # 继承 Animal 类
    # 该方法用来打印狗的叫声
    def say(self):
        print(f"{self._name} is making sound wang wang wang...")
