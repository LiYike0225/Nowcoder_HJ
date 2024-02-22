#数一串输入中元素的种类数
#string'' 添加语法是+=
#set{}用add
#list用append

res = set(input())
str = ''
for i in res:
    str += i
print(len(str))
