import sys

# DP, 배낭문제
# pypy3 기준으로는 시간 통과가 되나 python3로 시간초과 됨.
# memory를 기준으로 할시 범위가 너무 커지기 때문(10,000,001 칸을 사용)
# cost를 기준으로 인덱싱 할시 (10001 칸 만으로 가능) => 시간 효율 증가 => cost 기준 코드는 upgrade version 참조
#골드 3

INF=int(10**8)

N,need_memory=map(int,sys.stdin.readline().split())

Memory=list(map(int,sys.stdin.readline().split()))
cost=list(map(int,sys.stdin.readline().split()))

dp=[INF]*(need_memory+1)
dp[0]=0

# 메모리 기준 index
for i in range(N):
    need_time=cost[i]
    get_memory=Memory[i]
    for j in range(need_memory,-1,-1):
        memory_index= need_memory if (get_memory+j>need_memory) else get_memory+j
        dp[memory_index]=min(dp[memory_index],need_time+dp[j])
            
#print(dp)
print(dp[need_memory])