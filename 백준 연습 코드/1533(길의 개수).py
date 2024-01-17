import sys
# 수학, 그래프 이론, 분할 정복을 이용한 거듭 제곱
# 12850(본대산책2)의 응용 문제
# 간선 마다 걸리는 시간이 다른데 노드와 노드 사이에 새로운 노드를 추가해 모든 간선의 비용을 1로 맞춰 주면 된다.
# 플래티넘 3

N,start,end,time=map(int,sys.stdin.readline().split())

arr=[sys.stdin.readline().rstrip() for _ in range(N)]

# 인접행렬를 간선의 비용이 1이 되도록 재구성하기
world=[[0]*5*N for _ in range(5*N)]

for i in range(0,5*N,5):
    for j in range(1,5,1):
        world[i+j-1][i+j]=1

for i in range(N):
    for j in range(N):
        if(arr[i][j]!='0'):
            k=int(arr[i][j])
            world[5*i+k-1][5*j]=1

#print(world)

row=5*N
mod=1000003

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

matrix=fast_mastrix_power(time)

#print(matrix)
print(matrix[(start-1)*5][(end-1)*5]%mod)