import sys
from collections import deque

#구현, 시뮬레이션, BFS
#삼성 SW 역량 기출
#골드 2

dxdy=[(-1,0),(0,1),(1,0),(0,-1)]

#무지개 블록의 모든 위치를 찾아 반환하는 함수
def find_all_rainbow_position():
    rainbow_posion=[]
    
    for i in range(N):
        for j in range(N):
            if(world[i][j]==0):
                rainbow_posion.append((i,j))
    
    return rainbow_posion

# x,y 블록이 포함된 블록 그룹을 찾고 (블록크기, 무지개 개수, 행, 열, [블록그룹에 포함된 모든블록의 위치])를 반환하는 함수
def find_block_group(x,y,visited):
    que=deque()
    que.append((x,y))
    visited[x][y]=True
    
    block_size=0 
    rainbow_count=0
    block_positions=[]
    block_color=world[x][y]
    standard_position_x=x
    standard_position_y=y
    
    while(que):
        x,y=que.popleft()
        block_positions.append([x,y])
        
        block_size+=1
        if(world[x][y]==0):
            rainbow_count+=1
                    
        for dx,dy in dxdy:
            if(0<=x+dx<N and 0<=y+dy<N and (world[x+dx][y+dy]==0 or world[x+dx][y+dy]==block_color) and visited[x+dx][y+dy]==False):
                que.append([x+dx,y+dy])
                visited[x+dx][y+dy]=True

    return (block_size,rainbow_count,standard_position_x,standard_position_y,block_positions)


#  블록이 2개 이상인 가장 큰 블록그룹을 찾아 블록 그룹 정보를 반환하는 함수 (없다면 빈 리스트를 반환)
def find_biggest_group():
    rainbow_positions=find_all_rainbow_position()
    block_group=[] # 모든 블록 그룹의 정보를 담는 리스트
    visited=[[False]*N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            if(world[x][y]>0 and visited[x][y]==False):
                blocks=find_block_group(x,y,visited)
                if(blocks[0]>1): # 블록 그룹은 블록이 2개 이상이어야 함.
                    block_group.append(blocks)
                for rain_x,rain_y in rainbow_positions: # 다른 블록 그룹들에서도 레인보우 블록에 접근 가능하므로 레인보우 블록 방문을 초기화.
                    visited[rain_x][rain_y]=False 
                    
    if(block_group): 
        block_group.sort(reverse=True) # (크기, 무지개 블록 개수, 행, 열, [ 그룹에 해당하는 위치들]) 을 내림차순으로 정렬
        return block_group[0][4]
    else:
        return []

# 가장 큰 볼록 그룹의 블록들을 지우고 지운 개수를 반환하는 함수
def erase_biggest_group(positions):
    global world
    erase_count=0
    for x,y in positions:
        world[x][y]=-2 # -2가 빈칸의 의미
        erase_count+=1
    
    return erase_count

#  중력을 적용시켜 중력 적용 규칙에 맞게 블록을 이동시킨다.
def apply_gravity_to_block():
    global world
    new_world=[[-2]*N for _ in range(N)]

    for y in range(N):
        new_world_x=N-1
        for old_world_x in range(N-1,-1,-1):
            if(world[old_world_x][y]>=0):
                new_world[new_world_x][y]=world[old_world_x][y]
                new_world_x-=1
            elif(world[old_world_x][y]==-1):
                new_world_x=old_world_x
                new_world[new_world_x][y]=world[old_world_x][y]
                new_world_x-=1
    
    world=new_world

# 행렬을 반시계방향으로 90도 회전시키는 함수
def rotate_matrix_90_counter_clockwise():
    global world
    new_world=[[-2]*N for _ in range(N)] 
    
    for i in range(N):
        for j in range(N):
            new_world[N-1-j][i]=world[i][j]
    
    world=new_world

#main() 함수
N,M=map(int,sys.stdin.readline().split())
world=[]
for _ in range(N):
    world.append(list(map(int,sys.stdin.readline().split())))

total_point=0 # 총점(답)

while(True):
    biggest_block_positions=find_biggest_group() # 1) 가장 큰 블록그룹 찾기
    if(biggest_block_positions):
        erase_count=erase_biggest_group(biggest_block_positions)        # 2) 가장 큰 블록 그룹 맴버를 지우고 지운 개수를 반환
        total_point+=erase_count*erase_count # 3) 지운개수 * 지운 개수 만큼 점수를 획득
        apply_gravity_to_block() #4) 중력 적용
        rotate_matrix_90_counter_clockwise() #5) 90도 반시계방향으로 회전
        apply_gravity_to_block() #6) 중력 적용

    else: # 블록그룹이 존재 하지 않는 경우
        print(total_point)
        break