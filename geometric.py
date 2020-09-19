import math

def prob(n,p):
    ''' Hàm prob(n, p) tính xác suất của phân bố geometric ứng vói symbol X = n
        2 tham số đầu vào:  n - số lần thực hiện
                            p - xác suất tung được mặt ngửa
    '''
    return math.pow(1-p, n-1) * p
# print(prob(100,0.3))

def infoMeasure(n,p):
    ''' Hàm infoMeasure(n, p) tính lượng tin có các symbols theo phân bố geometric ứng với symbol X = n
        2 tham số đầu vào:  n - số lần thực hiện
                            p - xác suất tung được mặt ngửa
    '''
    return -math.log(prob(n,p)) / math.log(2)
# print(infoMeasure(100,0.3))

def sumProb(N,p):
    '''
    Sử dụng để kiểm chứng tổng xác suất của phân bố geometric bằng 1.
    Khi tăng giá trị của n lên thì giá trị trả về của hàm sumProb dần tiến đến 1.
    '''
    result = 0.0
    for i in range(1, N + 1):
        result = result + prob(i,p)
    return result
# print(sumProb(100,0.3))

def approxEntropy(N,p):
    '''
    Tính xấp xỉ entropy của nguồn tin geometric
    Với p = 1/2, N tiến đến vô cùng, approxEntropy(N,1/2) tiến đến 2
    '''
    result = 0.0
    for i in range (1, N + 1):
        result = result + prob(i,p) * infoMeasure(i,p)
    return result
# print(approxEntropy(100,0.5))

