class Book:
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print(f"书名：{self.name}")
