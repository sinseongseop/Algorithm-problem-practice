import sys
# 수학, 분할정복을 이용한 거듭 제곱
N=int(sys.stdin.readline())

# 인접 행렬
# 정보과학관,전산관,신양관,진리관,학생회관,형남공학관,한경직기념관,미래관 순 
world=[[0,1,0,0,0,0,0,1],
       [1,0,1,0,0,0,0,1],
       [0,1,0,1,0,0,1,1],
       [0,0,1,0,1,0,1,0],
       [0,0,0,1,0,1,0,0],
       [0,0,0,0,1,0,1,0],
       [0,0,1,1,0,1,0,1],
       [1,1,1,0,0,0,1,0]]

row=8
mod=1000000007

world_square=[[0]*row for _ in range(row)]
for i in range(row):
    for j in range(row):
        for k in range(row):
            world_square[i][j]+=world[i][k]*world[k][j]%mod

# 분할정복을 이용한 빠른 행렬 거듭제곱
def fast_mastrix_power(n):
    if(n==1):
        return world
    
    if(n==2):
        return world_square
    
    get_matrix=[[0]*row for _ in range(row)]
    matrix1=fast_mastrix_power(n//2)
    
    for i in range(row):
        for j in range(row):
            for k in range(row):
                get_matrix[i][j]+=matrix1[i][k]*matrix1[k][j]%mod
    
    if(n%2): # n이 홀수 인경우 (n//2)*(n//2)*1 과 동일
        get_matrix2=[[0]*row for _ in range(row)]
        for i in range(row):
            for j in range(row):
                for k in range(row):
                    get_matrix2[i][j]+=get_matrix[i][k]*world[k][j]%mod
        return get_matrix2 
  
    else: # n이 짝수 인경우 (n//2)*(n//2)과 동일
        return get_matrix

matrix=fast_mastrix_power(N)

print(matrix[0][0]%mod)
