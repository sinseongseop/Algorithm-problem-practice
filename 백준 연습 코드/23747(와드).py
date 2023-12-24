import sys
from collections import deque

row,column=map(int,sys.stdin.readline().split()) # 줄,컬럼 개수
world=[]
Seeing=[["#"]*column  for _ in range(row)] # 면 볼 수 없는 땅, . 면 볼 수 있는 땅 (출력 배열)
visit=[[False]*column for _ in range(row)] #bfs 탐색용 방문 표시 배열
dxdy=[[0,1],[1,0],[0,-1],[-1,0]] # 상하좌우 dx,dy 좌표들


for _ in range(row):
    world.append(sys.stdin.readline().rstrip()) #world 영역 알파벳 입력

positionX,positionY=map(int,sys.stdin.readline().split()) #초기 x,y 위치 입력
positionX-=1; positionY-=1 # x,y 위치를 배열 인덱스 0 부터 시작으로 통일
moving=sys.stdin.readline().rstrip() # 플레이어의 움직임

def CanSee(x,y): #x,y의 위치에 있을 때 터렛 없이도 볼 수 있는 땅을 "#"으로 바꾸는 함수
    Seeing[x][y]="."
    for dx,dy in dxdy:
        if(0<=x+dx<row and 0<=y+dy<column):
            Seeing[x+dx][y+dy]="."

def bfs(x,y,symbol): #같은 영역을 확인하는 BFS 함수
    que=deque()
    que.append([x,y])
    visit[x][y]=True
    while(que):
        x,y=que.popleft()
        Seeing[x][y]="."
        for dx,dy in dxdy:
            if(0<=x+dx<row and 0<=y+dy<column and world[x+dx][y+dy]==symbol and visit[x+dx][y+dy]==False):
                visit[x+dx][y+dy]=True
                que.append([x+dx,y+dy])
        
for instruction in moving:
    if(instruction=="L"): # 왼쪽 이동
        positionY-=1
    elif(instruction=="U"): # 위로 이동
        positionX-=1
    elif(instruction=="R"): # 오른쪽 이동       
        positionY+=1
    elif(instruction=="D"): # 아래로 이동
        positionX+=1
    else: #터렛 설치인 경우
        if(visit[positionX][positionY]==False):
            bfs(positionX,positionY,world[positionX][positionY])

CanSee(positionX,positionY)
for lineString in Seeing:
    for character in lineString:
        print(character,end="")
    print()
        


