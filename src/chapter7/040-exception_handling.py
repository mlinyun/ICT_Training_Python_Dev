"""异常处理"""

# try...except
while True:
    try:
        num = int(input("请输入一个整数（输入0结束输入）："))
        print(f"您输入的整数是：{num}")
        if num == 0:
            break
    except ValueError:
        print("您输入的好像不是一个整数")
        break
# 上面的例子中我们提前预判了 ValueError 错误
# 当我们不确定会遇到什么错误，也可以只写一个 except，而不注明具体会遇到的报错情况
# 不过这样写有一个问题，就是当问题出现时，我们看不到报错信息，就无法确定出现了的问题
# 所以，有时候我们也会使用 Exception 类
while True:
    try:
        num = int(input("请输入一个整数（输入0结束输入）："))
        print(f"您输入的整数是：{num}")
        if num == 0:
            break
    except Exception as e:
        print(e)  # 打印异常信息

# try..except...else
# try...except 语句还有一个可选的 else 子句，如果使用这个子句
# 那么必须放在所有的 except 子句的最后面
# else 子句将在 try 子句没有发生任何异常的时候执行
while True:
    try:
        num = float(input("请你输入一个数字作为除数："))
        result = 100 / num
    except ValueError as e:
        print("你输入的好像不是数字！")
        print(e)  # 打印异常信息
        break
    except ZeroDivisionError as e:
        print("除数不能为 0！")
        print(e)  # 打印异常信息
        break
    else:
        print(f"100 % {num} = {result:.2f}")
        break

# try...except...finally
# try...except 语句还有一个可选的 finally 子句，该子句不管 try 子句是否发生异常都会执行
while True:
    try:
        num = int(input("请输入一个整数："))
        print(f"您输入的整数是：{num}")
        break
    except ValueError as e:
        print("您输入的好像不是一个整数！")
        print(e)  # 打印异常信息
        break
    finally:
        print("=" * 20)

"""抛出异常"""
try:
    print(5 / 0)
except:
    print("除数不能为 0！")
    raise
