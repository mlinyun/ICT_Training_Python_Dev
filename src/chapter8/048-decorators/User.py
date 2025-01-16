# class User:
#     def __init__(self, name, email, password):
#         self.name = name
#         self.email = email
#         self._password = password

#     def get_password(self):
#         return self._password

#     def set_password(self, password):
#         self.p_assword = password

# 其中密码为关键数据，通常设置为私有属性，不可在类的外部直接调用
# 因此，设置了 get_password 和 set_password 两个方法用于获取密码和修改密码
# 这是没有问题的，唯一的小问题就是调用这两个方法来处理密码不如 name 和 email
# 那样方便，可以直接对属性进行赋值和获取值操作。此时，property 装饰器的机会就来了
# 它可以很好地解决这个小问题，将 User 类修改如下：
class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self._password = password

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    @password.deleter
    def password(self):
        del self._password

# 上面有三个装饰器装饰的函数（或方法），依次说明:
# 第一个方法，我们将 _password 属性的外部调用接口设为 password
# 用 property 装饰器定义此函数，返回值为实例的 _password 属性值
# 这样就定义好了获取 _password 属性值的方法

# 第二个方法，使用 password.setter 装饰器装饰 password 方法
# 注意装饰器的名字，点前面的 password 须与函数名相同
# 点后面的 setter 是固定的，不可修改。该方法用于修改实例的
# _password 属性的值，其中参数 password 的值就是新密码

# 第三个方法，可写可不写，它用于删除实例的 _password 属性
