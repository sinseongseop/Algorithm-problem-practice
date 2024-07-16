import sys
# 수학, 브루트포스 알고리즘
# 골드 5

N=int(sys.stdin.readline())
num= list(map(int,sys.stdin.readline().split()))
MAXCARD = 1000001

score=[[0,0] for _ in range(MAXCARD)] # (존재하는카드 여부, 점수)

for i in num: # 카드 존재 플래그 설정
    score[i][0]=1


for i in range(1,MAXCARD):
    if(score[i][0] == 1):
        for j in range(2*i, MAXCARD ,i):
            if(score[j][0]==1):
                score[i][1]+=1
                score[j][1]-=1

for i in num:
    print(score[i][1], end=" ")