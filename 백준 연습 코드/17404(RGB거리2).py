import sys
#DP
#첫번째 집의 색깔을 고정시킨 후 DP를 3번 돌린다.
#골드 4

INF=int(1000*1000)

N=int(sys.stdin.readline())
house=[]
for _ in range(N):
    house.append(list(map(int,sys.stdin.readline().split())))

min_cost=INF

for i in range(3): # 첫번째 집을 i번째 집으로 선택
    dp=[[INF]*3 for _ in range(N)]
    dp[0][i]=house[0][i]
    
    for j in range(1,N):
        dp[j][0]=min(dp[j-1][1],dp[j-1][2])+house[j][0]
        dp[j][1]=min(dp[j-1][0],dp[j-1][2])+house[j][1]
        dp[j][2]=min(dp[j-1][0],dp[j-1][1])+house[j][2]
    
    dp[N-1][i]=INF # 첫번째 집과 N번째 집의 색깔이 같으면 안되므로
    min_cost=min(min_cost,dp[N-1][0],dp[N-1][1],dp[N-1][2])
    #print(dp)
    
print(min_cost)