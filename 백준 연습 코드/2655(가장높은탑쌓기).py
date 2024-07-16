import sys

# DP, 정렬
# 골드3

# 입력 및 정렬
stoneCnt = int(sys.stdin.readline())
stones = []

for ithStone in range(1,stoneCnt+1):
    baseArea, height, weight = map(int,sys.stdin.readline().split())
    stones.append([baseArea, height, weight, ithStone]) # (넓이, 높이, 무게, 돌 번호)

stones.sort(reverse=True) # 넓이 내림차순으로 정렬
#print(stones) # 디버깅용

# dp 계산 : dp[i][j]는 i번째 돌로, 무게 순으로 j에 위치하는 돌을 선택했을때 최대값을 가지는 경우 
dp=[[[0,0,-1] for _ in range(stoneCnt)] for _ in range(stoneCnt)] #(총가치, 무게제한, 이전 돌 인덱스) 튜플을 원소로 가지는 이차원 배열

for i in range(stoneCnt):
    dp[0][i]=[stones[i][1],stones[i][2],-1]

for i in range(1,stoneCnt):
    for j in range(i,stoneCnt):
        for k in range(0,j):
            if( (dp[i-1][k][1] >= stones[j][2]) and (dp[i][j][0] < dp[i-1][k][0] + stones[j][1]) ):
                dp[i][j]=[dp[i-1][k][0]+stones[j][1], stones[j][2] ,k]
                
#print(dp) #디버깅용

# 최대 값 찾기
maxValue=0
maxIndex=0
for i in range(stoneCnt):
    for j in range(i,stoneCnt):
        if(maxValue < dp[i][j][0]):
            maxValue=dp[i][j][0]
            maxIndex=(i,j)
            
# 답 출력

print(maxIndex[0]+1) # 쌓은 돌의 개수

while(True):
    row=maxIndex[0]
    column=maxIndex[1]
    print(stones[column][3]) # 쌓은 돌의 번호
    if(dp[row][column][2]==-1):
        break
    else:
        maxIndex=(row-1,dp[row][column][2]) 
