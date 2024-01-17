import sys
#수학, 분할 정복을 이용한 거듭제곱

row,n=map(int,sys.stdin.readline().split())
arr1=[list(map(int,sys.stdin.readline().split())) for _ in range(row)]
arr_two=[[0]*row for _ in range(row)]
for i in range(row):
    for j in range(row):
        for k in range(row):
            arr_two[i][j]+=arr1[i][k]*arr1[k][j]%1000

# 분할정복을 이용한 빠른 행렬 거듭제곱
def fast_mastrix_power(n):
    if(n==1):
        return arr1
    
    if(n==2):
        return arr_two
    
    get_matrix=[[0]*row for _ in range(row)]
    matrix1=fast_mastrix_power(n//2)
    for i in range(row):
        for j in range(row):
            for k in range(row):
                get_matrix[i][j]+=matrix1[i][k]*matrix1[k][j]%1000
    
    if(n%2):
        get_matrix2=[[0]*row for _ in range(row)]
        for i in range(row):
            for j in range(row):
                for k in range(row):
                    get_matrix2[i][j]+=get_matrix[i][k]*arr1[k][j]%1000
        return get_matrix2
        
    else:
        return get_matrix

matrix=fast_mastrix_power(n)

for i in range(row):
    for j in range(row):
        print(matrix[i][j]%1000, end=" ")
    print()