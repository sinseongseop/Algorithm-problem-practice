import sys

# 자료 구조, 그래프 탐색, DFS, 분리 집합

direction={"D":(1,0), "L":(0,-1), "R":(0,1), "U":(-1,0)} # 각 문자별로 이동하는 방향
dxdy=[(1,0),(0,-1),(0,1),(-1,0)] # 남,서,동,북
same_part={0:"U",1:"R",2:"L",3:"D"} #dxdy와 연관, 한점을 기준으로 남쪽에 U, 서쪽에 R, 동쪽에 L, 북쪽에 D가 있는 각각의 경우 같은 영역이다.

# x,y와 같은 영역을 찾는 함수
def graph_search(x,y):
    global visited
    start=(x,y)
    stack=[(x,y)]
    
    visited[x][y]=True
    while(stack):
        x,y=stack.pop()
        dx,dy=direction[world[x][y]] 
        if(visited[x+dx][y+dy]==False): # 현재 있는 곳에서 다음으로 갈 수 있는 장소들 중 방문하지 않은 곳
            visited[x+dx][y+dy]=True
            stack.append((x+dx,y+dy))     
        
        for i in range(4): # 현재 있는 곳에 한번에 도달 가능한 장소들 중 아직 방문 하지 않은 곳
            dx,dy=dxdy[i]
            if(0<=x+dx<N and 0<=y+dy<M and visited[x+dx][y+dy]==False and world[x+dx][y+dy]==same_part[i]):
                visited[x+dx][y+dy]=True
                stack.append((x+dx,y+dy))
    

# main() 함수
N,M=map(int,sys.stdin.readline().split())
world=[]

for _ in range(N):
    world.append(sys.stdin.readline().rstrip())

visited=[[False]*M for _ in range(N)]

count=0
for x in range(N):
    for y in range(M):
        if(visited[x][y]==False):
            graph_search(x,y)
            count+=1
            #print(visited)
            
print(count)