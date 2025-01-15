string = input("请输入：")
str_list = string.split(" ")
print(f"生成的列表是：{str_list}")
str_list_re = str_list[::-1]
print(f"翻转后的列表是：{str_list_re}")
