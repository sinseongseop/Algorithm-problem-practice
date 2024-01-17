import sys

# DP, 배낭문제
# upgrade version
# pypy3 기준 - 메모리 기준 : 2740ms , 비용 기준: 120ms (23배 빨라짐)
# 골드 3

INF=int(10**8)

N,need_memory=map(int,sys.stdin.readline().split())

Memory=list(map(int,sys.stdin.readline().split()))
cost=list(map(int,sys.stdin.readline().split()))

#비용으로 index
dp=[-1]*(N*100+1) # N*100 +1 (개수 * 최대 비용 +1)
dp[0]=0

for i in range(N):
    need_time=cost[i]
    get_memory=Memory[i]
    for j in range(N*100,-1,-1):
        if(j-need_time<0):
            break
        if(dp[j-need_time]>=0):
            dp[j]=max(dp[j],dp[j-need_time]+get_memory)
              
#print(dp)
                    
for i in range(N*100+1):
    if(dp[i]>=need_memory): #최소비용 찾기
        print(i)
        break