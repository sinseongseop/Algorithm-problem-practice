import sys
from collections import deque
# 구현, 브루트포스, bfs
# 삼성 SW 기출
# 골드 4

N,M=map(int,sys.stdin.readline().split())

world=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]

def bfs(world,x,y,n,m): # 나머지 모양 탐색
    que=deque()
    que.append([x,y,1,0,-1,-1]) #(현재x,현재y,확장한칸수, 확장한 칸의 합, 이전x, 이전y)
    dxdy=[[0,1],[1,0],[-1,0],[0,-1]]
    big_num=0
    while(que):
        now_x,now_y,count,total,before_x,before_y=que.popleft()
        total+=world[now_x][now_y]
        if(count==4):
            big_num=max(big_num,total)
        else:
            for dx,dy in dxdy:
                if(0<=now_x+dx<n and 0<=now_y+dy<m and not (now_x+dx==before_x and now_y+dy==before_y)):
                    que.append([now_x+dx,now_y+dy,count+1,total,now_x,now_y])
    return big_num

max_num=0
for i in range(N):
    for j in range(M):
        if(j!=0 and j!=M-1): 
            if(i!=0): # ㅗ 모양
                max_num=max(max_num,world[i][j]+world[i-1][j]+world[i][j-1]+world[i][j+1])
            if(i!=N-1): # ㅜ 모양
                max_num=max(max_num,world[i][j]+world[i+1][j]+world[i][j-1]+world[i][j+1])
        if(i!=0 and i!=N-1):  
            if(j!=0): # ㅓ 모양
                max_num=max(max_num,world[i][j]+world[i][j-1]+world[i-1][j]+world[i+1][j])
            if(j!=M-1):  #ㅏ 모양
                max_num=max(max_num,world[i][j]+world[i][j+1]+world[i-1][j]+world[i+1][j])

for i in range(N):
    for j in range(M):  # 나머지 모양
        max_num=max(max_num,bfs(world,i,j,N,M))
print(max_num)