# 多态
import Cat
import Dog

cat = Cat.Cat("Kitty", 2)
print(cat.get_name())
print(cat.get_age())
cat.say()

dog = Dog.Dog("Ton", 4)
print(dog.get_name())
print(dog.get_age())
dog.set_name("Tony")
dog.set_age(3)
print(dog.get_name())
print(dog.get_age())
dog.say()
