import sys
import heapq

#구현, BFS, 우선순위큐, 시뮬레이션
# 삼성 SW 역량 테스트 기출 문제
# 골드 3

N=int(sys.stdin.readline())
world=[]

for _ in range(N):
    world.append(list(map(int,sys.stdin.readline().split())))

for i in range(N):
    for j in range(N):
        if(world[i][j]==9): # 초기 상어의 위치를 기억하고 0으로 바꿔준다.
            start_x=i
            start_y=j
            world[i][j]=0

shark_size=2 #상어 크기
shark_eat=0 # 상어가 먹은 음식양
total_time=0 # 총 소요시간

def bfs(x,y,time):
    global total_time, shark_eat,shark_size
    time_position=[(time,x,y)]  # 소요시간, x값, y값 순으로 원소가 작은게 먼저 나오는 우선순위 큐 
    heapq.heapify(time_position) 
    
    visited=[[False]*N for _ in range(N)] # 같은 곳 방문을 방지하기 위한 visit flag
    visited[x][y]=True
    dxdy=[(-1,0),(0,-1),(0,1),(1,0)]
    while(time_position):
        time,x,y=heapq.heappop(time_position)
        if(world[x][y]!=0 and world[x][y]<shark_size): # world[x][y]!=0 이고 상어가 먹을 수 있으면
            shark_eat+=1
            if(shark_eat>=shark_size): # 상어 크기 업데이트
                shark_size+=1
                shark_eat=0
            
            total_time+=time
            time=0
            world[x][y]=0

            time_position=[] # 먹이를 먹는 순간 다음 목적지를 처음 부터 새롭게 탐색
            visited=[[False]*N for _ in range(N)]
            visited[x][y]=True
            
            #for line in world:
            #    print(*line)
            #print()
                
        for dx,dy in dxdy: # 상하좌우 이동 가능한 땅 탐색 및 조건 부합시 우선순위큐에 추가
            if(0<= x+dx and x+dx<N and 0<=y+dy and y+dy<N and visited[x+dx][y+dy]==False and world[x+dx][y+dy]<=shark_size ):
                heapq.heappush(time_position,(time+1,x+dx,y+dy))
                visited[x+dx][y+dy]=True


#main()

bfs(start_x,start_y,0)
#print(world)
print(total_time)
    