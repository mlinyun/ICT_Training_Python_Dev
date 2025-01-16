class GithubSpider:
    name = "github"

    # 注意类方法的第一个参数传入的是类对象，而不是实例对象，所以是 cls
    # 类方法中要指代类对象本身都使用 cls
    @classmethod
    def get_name(cls):
        return cls.name
