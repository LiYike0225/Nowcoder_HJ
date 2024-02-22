# 输入一个 int 型的正整数，计算出该 int 型数据在内存中存储时 1 的个数。
# dec = int(input("输入数字："))
# print("十进制数为：", dec)
# print("转换为二进制为：", bin(dec))
# print("转换为八进制为：", oct(dec))
# print("转换为十六进制为：", hex(dec))
num = bin(int(input()))
str = (num[2:])
print(str.count('1'))