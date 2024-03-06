# 给出4个1-10的数字，通过加减乘除运算，得到数字为24就算胜利,除法指实数除法运算,运算符仅允许出现在两个数字之间,本题对数字选取顺序无要求，但每个数字仅允许使用一次，且需考虑括号运算
# # 此题允许数字重复，如3 3 4 4为合法输入，此输入一共有两个3，但是每个数字只允许使用一次，则运算过程中两个3都被选取并进行对应的计算操作

def is24(tes, tar):
    if tar < 1:
        return False

    if len(tes) == 1:
        return tes[0] == tar

    for i in range(len(tes)):
        nums = tes[:i] + tes[i + 1:]
        val = tes[i]
        if is24(nums, tar - val) or is24(nums, tar + val) or is24(nums, tar / val) or is24(nums, tar * val):
            return True
    return False

arr = list(map(int, input().split(' ')))#如果没有‘’会显示nonetype，导致len无法用
if is24(arr, 24):
    print("true")
else:
    print("false")
