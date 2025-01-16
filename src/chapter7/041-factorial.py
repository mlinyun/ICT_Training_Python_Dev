def calculate():
    x = input("请输入一个非负整数：")
    try:
        # 完善语句
        x = int(x)
        if x < 0:
            raise ValueError
    except ValueError:
        print('请输入非负整数')
    else:
        cal = x
        for i in range(1, cal):
            cal *= i
        print(f'{x}的阶乘为{cal}')


if __name__ == "__main__":
    calculate()
