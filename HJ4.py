while True:
    try:
        str = input()
        while len(str) > 8: #若等于8 则会出现 12345678 00000000的情况
            print(str[:8])
            str = str[8:]
        print(str.ljust(8,'0')) #ljust用于在不足8个ch的时候补齐
    except:
        break

