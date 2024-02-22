#输入一个 int 型整数，按照从右向左的阅读顺序，返回一个不含重复数字的新的整数。
#保证输入的整数最后一位不是 0
#str = reversed(input()) - reverse函数返回16进制值
str = input()
str = str[::-1]
empty_str= '' #establish an empty string
for i in str:
    if i not in empty_str:
        empty_str += i #add i to the empty string
print(empty_str)
