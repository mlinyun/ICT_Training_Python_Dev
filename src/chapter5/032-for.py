a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for 循环
for i in a:
    print(i)

# range() 函数
# 使用 range(x) 函数，可以生成一个从 0 到 x-1 的整数序列
for i in range(10):
    print(i)
# 还可以用 range(a,b) 取某个区间的数，比如要打印 1 到 10
for i in range(1, 11):
    print(i)
# range() 函数也支持步长
for i in range(1, 10, 2):
    print(i)
