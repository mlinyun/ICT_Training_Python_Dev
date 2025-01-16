import User
import GithubSpider
import Cat

user = User.User("Tom", "tom@gmail.com", "123456")
print(user.name)
print(user.email)
print(user.password)  # 打印密码
user.password = "654321"  # 修改密码
print(user.password)

# 类属性和类方法是可以直接使用类访问，不需要实例化
# 当然类的实例也是可以调用它们的
print(GithubSpider.GithubSpider.get_name())
# 可以直接修改类属性的值
GithubSpider.GithubSpider.name = "newGithub"
print(GithubSpider.GithubSpider.get_name())

# 静态方法在运行时不需要实例的参与，它被放在类下面只是因为它和类有一点关系
# 但并不像类方法那样需要传递一个 cls 参数
Cat.Cat.get_cat_food()
