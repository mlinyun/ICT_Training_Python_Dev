# 封装
import Cat
import Dog

# 创建猫实例
cat = Cat.Cat("Kitty")
print(cat.get_name())  # 通过 get_name 方法获取猫的名称
print(cat._name)  # 虽然可以访问，但约定为私有属性就是不要在类的外部直接调用
cat.say()  # 调用实例的 say 方法打印其叫声

# 创建狗实例
dog = Dog.Dog("Tom")
print(dog.get_name())
dog.set_name("Tony")  # 用实例的 set_name 方法改名
print(dog.get_name())
dog.say()
