import sys
sys.setrecursionlimit(10**4)

# DP, DFS
# 골드 3

dxdy=[(-1,0),(0,1),(1,0),(0,-1)]

def DFS(x,y):
    global dp
    
    if(dp[x][y]!=1):
        return dp[x][y]
    
    for dx,dy in dxdy:
        if(0<=x+dx<n and 0<=y+dy<n and world[x+dx][y+dy]<world[x][y]):
            move=DFS(x+dx,y+dy)
            dp[x][y]=max(dp[x][y],move+1)
    
    return dp[x][y]
        
n=int(sys.stdin.readline())
world=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
dp=[[1]*n for _ in range(n)]

max_move=1

for i in range(n):
    for j in range(n):
        move=DFS(i,j)
        max_move=max(max_move,move)

print(max_move)