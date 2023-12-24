import sys
#플로이드 워셜 알고리즘
INF=10e9

N=int(sys.stdin.readline())
bus=int(sys.stdin.readline())
arr=[[INF]*(N+1) for _ in range(N+1)]

for i in range(1,N+1):
    arr[i][i]=0

for _ in range(bus):
    start,end,cost=map(int,sys.stdin.readline().split())
    arr[start][end]=min(arr[start][end],cost)
    
for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            arr[i][j]=min(arr[i][k]+arr[k][j],arr[i][j])

for i in range(1,N+1):
    for j in range(1,N+1):
        if(arr[i][j]==INF):
            print(0, end=" ")
        else:
            print(arr[i][j], end=" ")
    print()   