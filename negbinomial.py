import math
def giaiThua(m):
    if(m == 1 or m == 0):
        return 1
    else:
        return m * giaiThua(m - 1)
# print(giaiThua(100))

def prob(n,p,r):
    ''' Hàm prob(n, p, r) tính xác suất của phân bố negative binomial
        3 tham số đầu vào:  n - symbol đang cần tính xác suất
                            p - xác suất Bernoulli (tung được mặt ngửa)
                            r - số lần tung được mặt ngửa cần đạt được
    '''
    q = (p ** r) * ((1 - p) ** (n - r))
    if n < r:
        return 0
    return giaiThua(n - 1) / ((giaiThua(n - r)) * giaiThua(r - 1)) * q
# print(prob(10,0.2,5))

def infoMeasure(N,p,r):  
    ''' Hàm infoMeasure(N, p, r) tính lượng tin có các symbols theo phân bố negative binomial
        3 tham số đầu vào:  N - tổng số lần thực hiện
                            p - xác suất Bernoulli (tung được mặt ngửa)
                            r - số lần tung được mặt ngửa cần đạt được
    '''
    if N < r:
        return 0
    return -math.log(prob(N,p,r)) / math.log(2)
# print(infoMeasure(100,0.2,10))

def sumProb(N,p,r):
    ''' Hàm sumProb(n,p) tính giá trị tổng xác suất của các symbol từ r đến N cho nguồn có các symbol theo phân bố negative binomial
        với N là tổng số phép thử
    '''
    result = 0.0
    for i in range (r, N + 1):
        result = result + prob(i,p,r)
    return result
# print(sumProb(50,0.6,10))

def approxEntropy(N,p,r):
    '''
    Tính xấp xỉ entropy của nguồn tin geometric
    Với p = 1/2, N tiến đến vô cùng, approxEntropy() tiến đến 2
    '''
    result = 0.0
    for i in range (r, N + 1):
        result = result + prob(i,p,r) * infoMeasure(i,p,r)
    return result
# print(approxEntropy(50,1/2,10))

