"""
以下の関数郡を完成させましょう．
実際に処理が正しいかどうかは，電卓もしくは正しく計算してくれるwebサイトなどを用いて確認しましょう．
*pass構文は削除してください．
*sqrt関数はいじる必要はありません．
"""


import math

def sqrt(x):
    # input : 数値x
    # output : xの平方根

    return math.sqrt(x)

def square(x):
    # input : 数値x
    # output : xの二乗
    pass

def mean(xi):
    # input : 数値集合xi(リスト)
    # output : xiの平均

    pass

def deviation(x, xi):
    # input : 数値xと，そのxが属する数値集合xi(リスト)
    # output : xとxiの偏差
    pass

def variance(xi):
    # input : 数値集合xi(リスト)
    # output : xiの分散
    pass

def standard_dev(xi):
    # input : 数値集合xi(リスト)
    # output : xiの標準偏差
    pass


if __name__ == '__main__':

    data = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

    print(square(sqrt(2)))
    print(mean(data))
    print(variance(data))
    print(standard_dev(data))



