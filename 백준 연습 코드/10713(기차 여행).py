import sys

# 누적합
# 골드 4

N, M = map(int, sys.stdin.readline().split())
travelCity = list(map(int, sys.stdin.readline().split())) # 방문하는 도시 순서
cost = [list(map(int, input().split())) for _ in range(N-1)]
    
count = [0]*(N+1) # 누적합

for i in range(M-1):
    start, end= travelCity[i], travelCity[i+1]
    if(start> end):
        start, end = end, start
    count[start] += 1
    count[end] -= 1

#print(count) # 디버깅용
answer = 0 
total = 0
for i in range(1,N):
    total += count[i]
    answer += min(cost[i-1][0]*total, cost[i-1][1]*total + cost[i-1][2])

print(answer)