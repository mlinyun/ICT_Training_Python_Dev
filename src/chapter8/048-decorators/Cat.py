class Cat:
    owner = "张三"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def get_cat_food():
        # 静态方法可以调用类属性，但是不能够直接调用
        # 正确方式是使用 __class__ 代替类本身来调用类方法
        # print(f"{owner}去超市...")  # 报错
        print(f"{__class__.owner}去超市...")
        print("买猫粮...")
        print("回家...")
