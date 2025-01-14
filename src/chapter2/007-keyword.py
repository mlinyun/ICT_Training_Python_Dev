# 关键字(保留字)和预定义标识符
import keyword

print("Python 中包含的关键字如下：")
keyword_list = keyword.kwlist
print(keyword_list)
print(f"Python 中包含的关键字数量为：{len(keyword_list)}")

print()

print("Python 语言有很多预定义标识符，其中包括内置函数、内置对象、内置异常、内置常量：")
builtins = dir(__builtins__)
print(builtins)
print(f"Python 中包含的预定义标识符数量为：{len(builtins)}")
# 一般不建议将预定义标识符当作用户标识符使用，主要原因是容易引起混乱
# 比如下面的例子，我们给 print赋值让它等于 5，然后我们想要打印字符的时候 print 函数就无法使用了
# print = 5
# print("hello")
