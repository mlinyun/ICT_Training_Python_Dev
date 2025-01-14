import sys

# Python3 默认编码方式
conding = sys.getdefaultencoding()

print(f"Python3 的默认编码方式：{conding}")

# 在 Python 3 中，字符串是使用 unicode 编码的，所以我们可以通过内置函数 ord() 获得单字符对应的 unicode 十进制整数
char_a = ord("a")
print(f"字符 'a' 对应的 Unicode 十进制整数：{char_a}")
char_wo = ord("我")
print(f"字符 '我' 对应的 Unicode 十进制整数：{char_wo}")
char_semicolon = ord(";")
print(f"字符 ';' 对应的 Unicode 十进制整数：{char_semicolon}")

# 通过内置函数 chr() 获得十进制整数或者十六进制的整数对应的 unicode 编码
char_zhong = chr(20013)
print(f"Unicode 十进制整数 20013 对应的字符：{char_zhong}")
char_guo = chr(22269)
print(f"Unicode 十进制整数 22269 对应的字符：{char_guo}")
char_ren = chr(0x4eba)  # 十六进制数字一般以 0x 开头来表示 # 十六进制数字一般以 0x 开头来表示
print(f"Unicode 十六进制整数 0x4eba 对应的字符：{char_ren}")

# 将十进制的整数转换为十六进制的整数
hex_ren = hex(ord("人"))
print(f"字符 '人' 对应的 Unicode 十六进制整数：{hex_ren}")

# encode(编码) 方法和 decode(解码) 方法
# encode() 方法以指定的编码格式编码字符串。该方法返回编码后的字符串是一个 bytes 对象
# 目标：把字符串 "我是谁" 分别转换为 utf-8 和 gbk
string = "我是谁"
string_utf8 = string.encode("utf-8")
print(f"字符串 '我是谁' 转换为 utf-8 编码：{string_utf8}")
string_gbk = string.encode("gbk")
print(f"字符串 '我是谁' 转换为 gbk 编码：{string_gbk}")
# decode() 方法可以用指定的编码格式解码 bytes 对象
string_utf8_decode = string_utf8.decode("utf-8")
print(f"utf-8 编码的 {string_utf8} 转换为字符串：{string_utf8_decode}")
string_gbk_decode = string_gbk.decode("gbk")
print(f"gbk 编码的 {string_gbk} 转换为字符串：{string_gbk_decode}")
# 使用错误的编码格式进行解码(报错)
# print(string_gbk.decode("utf-8"))
# UnicodeDecodeError: 'utf-8' codec can't decode byte 0xc0 in position 0: invalid start byte