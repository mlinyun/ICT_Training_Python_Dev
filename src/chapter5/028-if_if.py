age = int(input("请输入您的年龄："))

if age >= 60:
    if age >= 70:
        print("免费")
    else:
        print("半价")
else:
    print("原价")
