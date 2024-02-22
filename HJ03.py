while True:
    try:
        n = int(input(''))
        res = set()
        for i in range(n):
            res.add(int(input()))
        for j in sorted(res):
            print(j)
    except:
        break

