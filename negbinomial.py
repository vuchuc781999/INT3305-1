import math


def factorial(n, calculatedN=1, calculatedFactorial=1):
    '''
    Tính giai thừa dựa vào giá trị gia thừa có hệ số nhỏ hơn đã được tính
    '''
    if n <= calculatedN:
        return calculatedFactorial

    return factorial(n - 1, calculatedN, calculatedFactorial) * n


def prob(n, p, r):
    if n - r + 1 < n / 2:
        a = factorial(n - r + 1)
        b = factorial(r - 1, n - r + 1, a)
        c = factorial(n, r - 1, b)
    else:
        a = factorial(r - 1)
        b = factorial(n - r + 1, r - 1, a)
        c = factorial(n, n - r + 1, b)

    return (c / (a * b)) * (p ** n) * ((1 - p)**r)


def infoMeasure(n, p, r):
    return -math.log2(prob(n, p, r))


def sumProb(N, p, r):
    sum = 0
    for i in range(1, N + 1):
        sum += prob(i, p, r)

    return sum


def approxEntropy(N, p, r):
    sum = 0
    for i in range(1, N + 1):
        temp = prob(i, p, r)
        sum += temp * (-math.log2(temp))

    return sum
