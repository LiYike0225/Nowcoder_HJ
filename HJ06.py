# 找出正整数的质因子，并按顺序输出
# 怎么解决重复质数的问题 - 不用set()
# 大于sqrt(n)的质因数只有一个
# 以下代码运行超时 - 对于如71这样的质数需运行71次
import math

# while True:
#     try:
#         num = int(input())
#         prime_num = 2
#         res = []
#         while prime_num <= num:
#             if num % prime_num == 0:
#                 res.append(prime_num)
#                 num = num/prime_num
#             else:
#                 prime_num += 1
#         for i in (sorted(res)):
#             print(i, end = ' ')
#     except:
#         break
num = int(input())
def is_prime(num):
    prime_num = 1
    for i in range(2, int(num**0.5+1)):
        if num % i == 0: #num非质数
            prime_num = 0
            print(int(i),end=' ')
            num = int(num/i)
            is_prime(num)
            break
    if prime_num == 1:
        print(num,end=' ')
is_prime(num)
#算法逻辑 - 若num是质数，输出num
#若num不是质数，num最大质因子不超过算数平方根，用递归找算数平方根的质因子，减少时间复杂度

