# 合法坐标为A(或者D或者W或者S) + 数字（两位以内）
#
# 坐标之间以;分隔。
#
# 非法坐标点需要进行丢弃。如AA10;  A1A;  $%$;  YAD; 等

(ini_x,ini_y) = (0,0)
input_list = input().split(';')
direction_list=('ADSW')
d = {} #创建一个空字典
#i[0]是一个directionlist中的字母，若i[1：]是一个整数，那么可以在空字典中存储对应的坐标移动量
#取d{[i[0]}中的值并且加上i后的整数量，此时注意判断i[1:]是否是整数，不然会报错
#if判断中将ADSWkey中对应的值相加，最后坐标AD相减，SW相减即可
#若字符串长度小于1，如A，会导致string index out of range
for i in input_list:
    if len(i)>1 and i[0] in direction_list and i[1:].isdecimal():
        d[i[0]] = d.get(i[0],0) + int(i[1:])
    else:
        pass
ini_x = d['D']-d['A']
ini_y = d['W']-d['S']
print(str(ini_x)+','+str(ini_y))




