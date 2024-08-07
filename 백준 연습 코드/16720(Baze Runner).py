import sys

#애드혹, 그리디
#실버 1

N= int(sys.stdin.readline())
maze=[sys.stdin.readline().strip() for _ in range(N-2)]

lineRoadCnt=[0]*4

#각 라인별로 현재 길의 개수
for i in range(N-2):
    for j in range(4):
        if(maze[i][j] == '0'):
            lineRoadCnt[j]+=1

moveCnt=N+2

#print(lineRoadCnt) #디버깅용

moveCnt+=min(lineRoadCnt[1]+2*lineRoadCnt[2]+lineRoadCnt[3], 
            lineRoadCnt[0]+lineRoadCnt[2]+2*lineRoadCnt[3],
            2*lineRoadCnt[0]+lineRoadCnt[1]+lineRoadCnt[3],
            lineRoadCnt[0]+2*lineRoadCnt[1]+lineRoadCnt[2]
            )

print(moveCnt)