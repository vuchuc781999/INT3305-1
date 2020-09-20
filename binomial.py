import math


def factorial(n, calculatedN=1, calculatedFactorial=1):
    '''
    Tính giai thừa dựa vào giá trị gia thừa có hệ số nhỏ hơn đã được tính
    '''
    if n <= calculatedN:
        return calculatedFactorial

    return factorial(n - 1, calculatedN, calculatedFactorial) * n


def prob(n, p, N):
    if n < N / 2:
        a = factorial(n)
        b = factorial(N - n, n, a)
        c = factorial(N, N - n, b)
    else:
        a = factorial(N - n)
        b = factorial(n, N - n, a)
        c = factorial(N, n, b)

    return (c / (a * b)) * (p ** n) * ((1 - p)**(N - n))


def infoMeasure(n, p, N):
    return -math.log2(prob(n, p, N))


def sumProb(N, p):
    sum = 0
    for i in range(1, N + 1):
        sum += prob(i, p, N)

    return sum


def approxEntropy(N, p):
    sum = 0
    for i in range(1, N + 1):
        temp = prob(i, p, N)
        sum += temp * (-math.log2(temp))

    return sum
