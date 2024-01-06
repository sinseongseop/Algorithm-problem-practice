import sys
# DP, 트리 DP
# 상사는 무조건 본인보다 번호가 작은 사람만 가능하다. 개인 별 칭찬을 한번에 다 반영하고 그 후 ID=0 인 사람 부터 차례대로 자신의 상사가 받은 칭찬 수치만큼을 자신 한테 더해 주면 된다.
# 골드 4

N,M=map(int,sys.stdin.readline().split())

bossArray=list(map(int,sys.stdin.readline().split())) # 자신의 상사가 누군지를 담은 배열

dp=[0]*(N+1)

# 칭찬 업데이트
for _ in range(M):
    people_id,weight=map(int,sys.stdin.readline().split())
    dp[people_id]+=weight

# 상사로부터 칭찬 받기
for i in range(1,N):
    dp[i+1]+=dp[bossArray[i]]

# 답
for i in dp[1:]:
    print(i,end=" ")
