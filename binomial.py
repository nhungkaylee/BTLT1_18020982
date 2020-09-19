import math
def giaiThua(m):
    if(m == 1 or m == 0):
        return 1
    else:
        return m * giaiThua(m - 1)
# print(giaiThua(5))

def prob(n,p,N):
    ''' Hàm prob(n, p, N) tính xác suất của phân bố binomial
        3 tham số đầu vào:  n - số lần tung thành công mặt ngửa
                            p - xác suất tung được mặt ngửa
                            N - tổng số lần thực hiện
    '''
    q = (p ** n) * ((1 - p) ** (N - n))
    return giaiThua(N) / ( giaiThua(N - n) * giaiThua (n)) * q
# print(prop(3,0.5,5))

def infoMeasure(n,p,N):
    ''' Hàm infoMeasure(n, p, N) tính lượng tin có các symbols theo phân bố binomial
        3 tham số đầu vào:  n - số lần tung thành công mặt ngửa
                            p - xác suất tung được mặt ngửa
                            N - tổng số lần thực hiện
    '''
    return -math.log(prob(n,p,N)) / math.log(2)
# print(infoMeasure(3,0.3,5))

def sumProb(N,p):
    ''' Hàm sumProb(N,p) tính giá trị tổng xác suất của các symbol từ 1 đến N cho nguồn có các symbol theo phân bố binomial 
        Với N là tổng số phép thử
    '''
    result = 0.0
    for i in range (1, N + 1):
        result = result + prob(i,p,N)
    return result
# print(sumProb(100,0.6))

def approxEntropy(N,p):
    '''
    Hàm approxEntropy(N, p) tính giá trị trung bình lượng tin của tất cả symbol từ 1 đến N
    với N là tổng số phép thử
    Tính xấp xỉ entropy của nguồn tin geometric
    '''
    result = 0.0
    for i in range (1, N + 1):
        result = result + prob(i,p,N) * infoMeasure(i,p,N)
    return result
# print(approxEntropy(100,1/2))