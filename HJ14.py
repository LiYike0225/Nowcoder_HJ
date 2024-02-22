# 输入第一行为一个正整数n(1≤n≤1000),下面n行为n个字符串(字符串长度≤100),字符串中只含有大小写字母。
#和随机数不同，不能创建集合，因为存在重复元素，应该用元组或者list
num = int(input())
list = list()
i = 1
while i <= num:
    list.append(input())
    i += 1
for i in sorted(list):
    print(i)