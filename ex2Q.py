#関数の問題
# ex3にオブジェクト指向の問題

# 関数 for リスト表現
import math

def square(x):
    return x*x

def sqrt(x):
    return math.sqrt(x)

def mean(xi):
    xilen = len(xi)
    sum = 0
    for x in xi:
        sum += x

    return sum/xilen

def deviation(x, xi):
    # 数値と数値のリストを入力にする
    return x - mean(xi)

def variance(xi):
    xilen = len(xi)
    sum_of_squared_dev = 0
    for x in xi:
        sum_of_squared_dev += square(deviation(x, xi))

    return sum_of_squared_dev/xilen

def standard_dev(xi):
    return sqrt(variance(xi))



if __name__ == '__main__':
    data = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    print(mean(data))
    print(variance(data))
    print(square(sqrt(8)))
    print(standard_dev(data))



