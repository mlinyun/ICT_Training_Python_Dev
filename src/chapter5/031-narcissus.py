import math

num = int(input("请输入一个三位数："))
temp = num
num_sum = 0
while temp > 0:
    num_sum += math.pow(temp % 10, 3)
    temp //= 10

if num_sum == num:
    print(f"{num}是水仙花数")
else:
    print(f"{num}不是水仙花数")
