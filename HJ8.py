#合并表记录
#dic.get(index.0)就是找出index所对应的value，若没有则按照0处理
pairs = int(input())
dic = {}
for i in range(pairs):
    line = input().split()
    index = int(line[0])
    value = int(line[1])
    dic[index] = dic.get(index,0) + value
for key in sorted(dic):
    print(key, dic[key])
