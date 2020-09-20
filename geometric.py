import math


def prob(n, p):
    return ((1 - p) ** (n - 1)) * p


def infoMeasure(n, p):
    return -math.log2(prob(n, p))


def sumProb(N, p):
    '''
    Ta có thể chứng minh tổng xác xuất của phân bố Geometric bằng 1 bằng cách
    truyền vào một giá trị N đủ lớn (1000). Giá trị trả về được làm tròn và
    hiển thị (1.0) đủ để kết luận điều trên. 
    '''
    sum = 0
    for n in range(1, N + 1):
        sum += prob(n, p)

    return sum


def approxEntropy(N, p):
    '''
    Tính entropy của nguồn thông tin geometric chính là thực hiện hàm 
    approxEntropy với giá trị của N là dương vô cùng. Vì thế ta có thể tính
    sấp xỉ entropy với giá trị của N truyền vào đủ lớn. Với p = 1/2 và N =
    1000 giá trị trả về xấp xỉ 2 (1.9999999999999998)
    '''
    sum = 0
    for n in range(0, N + 1):
        temp = prob(n, p)
        sum += temp * (-math.log2(temp))

    return sum
