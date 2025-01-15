# break 表示停止当前循环
for a in range(10):
    if a == 5:
        break
    print(a)

# continue 表示跳过本轮循环，去执行下一轮循环
a = 0
while a < 10:
    a = a + 1
    if a == 5:
        continue
    print(a)
