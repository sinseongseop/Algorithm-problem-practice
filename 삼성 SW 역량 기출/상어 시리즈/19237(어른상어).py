import sys
#구현, 시뮬레이션

#냄새 업데이트 함수
def update_smell():
    for i in range(N):
        for j in range(N):
            if(smell[i][j][1]!=0): # 냄새가 남아 있으면 남은 냄새 지속시간 감소
                smell[i][j][1]-=1
                if(smell[i][j][1]==0): # 냄새 지속시간이 0 이면 i,j 위치를 빈칸으로
                    smell[i][j]=[0,0]

            if(world[i][j]!=0): # 상어가 위치한 장소라면
                smell[i][j]=[world[i][j],K] 


dxdy=[[0,0],[-1,0],[1,0],[0,-1],[0,1]]

# 상어 움직임 업데이트 함수
def move_shark():
    INF=int(100000)
    shark_count=0
    new_shark_position=[[INF]*N for _ in range(N)] #상어가 이동할 자리
    for i in range(N):
        for j in range(N):
            if(world[i][j]!=0):
                sharkHeading=shark_direction[world[i][j]] # 상어가 바라보는 방향
                determine_direct=False # 갈 방향이 결정되었는지 flag
                for k in range(4):
                    dx,dy=dxdy[direction_priority[world[i][j]][sharkHeading][k]]
                    if(0<=i+dx<N and 0<=j+dy<N and smell[i+dx][j+dy][1]==0): # 냄새가 없는 곳이 우선
                        new_shark_position[i+dx][j+dy]=min(new_shark_position[i+dx][j+dy], world[i][j]) # 한 공간에 두마리 이상이 동시에 있을 시 번호가 작은 상어만 남음
                        shark_direction[world[i][j]]=direction_priority[world[i][j]][sharkHeading][k] # 이동 후 상어가 가지는 방향
                        determine_direct=True 
                        break
                
                if(determine_direct==False): # 냄새가 없는 곳이 없는 경우 본인의 냄새 위치로 이동
                    for k in range(4):
                        dx,dy=dxdy[direction_priority[world[i][j]][sharkHeading][k]]
                        if(0<=i+dx<N and 0<=j+dy<N and smell[i+dx][j+dy][0]==world[i][j]):
                            new_shark_position[i+dx][j+dy]=min(new_shark_position[i+dx][j+dy],world[i][j])
                            shark_direction[world[i][j]]=direction_priority[world[i][j]][sharkHeading][k]
                            determine_direct=True
                            break
    
    for i in range(N): # world에 새로운 world 업데이트
        for j in range(N):
            if(new_shark_position[i][j]==INF):
                world[i][j]=0
            else:
                world[i][j]=new_shark_position[i][j]
                shark_count+=1
    return shark_count

# main() 함수
N,M,K=map(int,sys.stdin.readline().split())
world=[]

# 초기 상어 위치 설정
for _ in range(N):
    world.append(list(map(int,sys.stdin.readline().split())))

#초기 상어 방향 설정
shark_direction=[0]
shark_direction+=list(map(int,sys.stdin.readline().split()))

# 상어별 방향 우선순위 설정
direction_priority=[[]]
for _ in range(M):
    shark_priority=[[]]
    for i in range(4):
        priority=list(map(int,sys.stdin.readline().split()))
        shark_priority.append(priority)
    direction_priority.append(shark_priority)


#초기 냄새 설정
smell=[]
for _ in range(N):
    row_smell=[]
    for i in range(N):
        row_smell.append([0,0])
    smell.append(row_smell)

#print(smell)

for i in range(N):
    for j in range(N):
        if(world[i][j]!=0):
            smell[i][j]=[world[i][j],K]
            
time=0 # 총소요 시간 (답안)
shark_count=M # 남은 상어 수

while(shark_count>1 and time<=1000):
    shark_count=move_shark()
    update_smell()
    time+=1

if(time<=1000):
    print(time)
else:
    print(-1)