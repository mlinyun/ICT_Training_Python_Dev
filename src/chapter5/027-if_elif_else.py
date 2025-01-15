age = int(input("请输入您的年龄："))

if 70 > age >= 60:
    print("半价")
elif age >= 70:
    print("免费")
else:
    print("原价")
