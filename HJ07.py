#浮点数四舍五入
num = float(input())
if (num-int(num)) >= 0.5:
    num = int(num)+1
else:
    num = int(num)
print(num)
