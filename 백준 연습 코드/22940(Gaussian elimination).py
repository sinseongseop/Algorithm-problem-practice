import sys

N=int(sys.stdin.readline())
arr=[list(map(int,sys.stdin.readline().split())) for _ in range(N) ]
for i in range(N-1):
    for j in range(i+1,N):
        pivot=arr[j][i]/arr[i][i]
        for k in range(i,N+1):
            arr[j][k]=arr[j][k]-pivot*arr[i][k]
    #print(arr) #중간 과정 확인용
        
answer=[0]*N
for i in range(N-1,-1,-1):
    for k in range(N-1,i-1,-1):        
        if(i!=k):
            arr[i][N]-=arr[i][k]*answer[k]
        else:
            answer[k]=int(round(arr[i][N]/arr[i][k]))
for i in answer:
    print(i,end=" ")