# 继承
import Cat
import Dog

cat = Cat.Cat("Kitty")
print(cat.get_name())
cat.say()

dog = Dog.Dog("Tom")
print(dog.get_name())
dog.set_name("Tony")
print(dog.get_name())
dog.say()
