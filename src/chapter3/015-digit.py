number = int(input("请输入一个四位数："))
digit_sum = 0  # 表示数字之和

temp = number

while temp > 0:
    digit_sum = digit_sum + temp % 10
    temp //= 10

print(f"{number}的个位数之和为：{digit_sum}")
