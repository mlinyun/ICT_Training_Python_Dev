# 文件操作
# 文件的读写

"""写入文件"""
# 打开一个文件
f = open("./data/poem.txt", "w")
# 在文件中写入内容
f.write("床前明月光，\n疑似地上霜。\n举头望明月，\n低头思故乡。")
# 关闭打开的文件
f.close()

# 上面的例子是普通的用法，Python 官方更推荐使用 with 关键字进行文件的操作。上面的代码可以修改如下：
with open("./data/poem.txt", "w") as f:
    f.write("床前明月光，\n疑似地上霜。\n举头望明月，\n低头思故乡。")

# 这种 with 关键字的用法让代码变得更简短，子句体结束后，文件会正确关闭，不需要我们去操作，即便触发异常也可以


"""读取文件"""
# 写入文件时我们使用了 write() 方法，读取文件的时候我们三种选择，read()、readline() 和 readlines()

# read(size) 方法有个可选参数 size，当省略 size 或者 size 的值为负数时，表示读取全部内容
# 当 size 取其他值时，就会读取并返回 size 个字符（文本模式）或 size 个字节（二进制模式）
f = open("./data/poem.txt", "r")
# poem_all = f.read()
# print(poem_all)
# 注意，运行下面的代码需要将上面读取所有的代码注释，因为读取文件是从头开始的，读取到文件末尾时，再读取就会返回空字符串
poem_13 = f.read(13)
print(poem_13)
# 把剩余的字符全部读取出来
print(f.read())
print()
f.close()

# read() 方法是按字符或字节读取的，而 readline() 方法是按行读取的
f = open("data/poem.txt")
poem_line = f.readline()
print(poem_line)
# poem.txt 文件一共有 4 行，现在我们只读了 1 行，就是说还可以再继续读取
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())  # 这里读取的为空
f.close()

# readlines() 可以返回文件的所有行
f = open("data/poem.txt")
poem_lines = f.readlines()
print(poem_lines)
f.close()
