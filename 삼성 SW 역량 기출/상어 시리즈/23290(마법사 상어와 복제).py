import sys
import copy
# 구현, 시뮬레이션
# 삼성 SW 기출
# 난이도 사악, 구현량 상당히 많음. 예외 처리 신경 많이 써야함.
#골드 1

fish_dxdy=[(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)] # 물고기가 움직이는 방향
shark_dxdy=[(-1,0),(0,-1),(1,0),(0,1)] # 상어가 움직이는 방향

# 모든 물고기를 이동시키는 함수
def all_fish_move():
    global world,fish_count_array
    new_world=[[[] for _ in range(4)] for _ in range(4)]
    new_fish_count=[[0]*4 for _ in range(4)]
    for x in range(4):
        for y in range(4):
            for fish_direction in world[x][y]:
                start_direction=fish_direction 
                while(True):
                    dx,dy=fish_dxdy[fish_direction%8]
                    if(0<=x+dx<4 and 0<=y+dy<4 and fish_smell[x+dx][y+dy]==0 and shark_position!=[x+dx,y+dy]):
                        new_world[x+dx][y+dy].append(fish_direction%8)
                        new_fish_count[x+dx][y+dy]+=1
                        break
                    else:
                        fish_direction-=1 # 45도 반시계 방향으로 방향 회전
                        if((fish_direction%8)==start_direction): # 8 방향을 다 확인 했는 데도 갈 수 없으면 이동을 안함.
                            new_world[x][y].append(start_direction)
                            new_fish_count[x][y]+=1
                            break
   
    # 업데이트
    world=new_world 
    fish_count_array=new_fish_count

# 상어가 움직이는 최적의 경로를 찾는 함수
def find_shark_root(turn,position ,total_eat_fish, moving,visit):
    max_total_fish=-1 # 최대로 많이 잡아 먹는 물고기 수
    max_shark_moving=[] # 최적 경로
    shark_x,shark_y=position

    if(position not in visit): # 방문 한적 있는 곳에 또 방문 가능함. 단 물고기 두번 카운트 되는 걸 방지하는 조건문 필요 ex) 왼 오 오 가능
        total_eat_fish+=fish_count_array[shark_x][shark_y]
    
    if(turn!=0): # 상어의 초기 위치는 방문 처리 하면 안됨
        visit.append(position)
    
    if(turn==3): # 3번 움직이고 나면 경로에 있는 총 물고기, 움직임 반환
        visit.pop()
        return (total_eat_fish,moving)

    for i in range(4):
        dx,dy=shark_dxdy[i]
        if(0<=shark_x+dx<4 and 0<=shark_y+dy<4):
            eat_fishes,root = find_shark_root(turn+1,[shark_x+dx,shark_y+dy],total_eat_fish,moving+[i],visit)

            if(eat_fishes>max_total_fish): #최대 물고기 인 경우 업데이트
                max_total_fish=eat_fishes
                max_shark_moving=root

    if(visit): 
        visit.pop()
        
    return max_total_fish,max_shark_moving # 최대 물고기, 최대 경로 반환

# 3칸 연속으로 상어가 움직임
def shark_move():
    shark_moving=[]
    global shark_position
    max_total_fish,shark_moving=find_shark_root(0,shark_position,0,[],[]) # 상어가 움직일 경로 탐색.
    for direction in shark_moving: # 상어가 3번 움직임
        dx,dy=shark_dxdy[direction]
        move_x=shark_position[0]+dx
        move_y=shark_position[1]+dy
        shark_position=[move_x, move_y]
        if(fish_count_array[move_x][move_y]!=0): #상어가 움직이는 곳에 물고기가 존재하면
            world[move_x][move_y]=[]
            fish_smell[move_x][move_y]=3 # 상어를 움직인 다음에 바로 냄새를 1 감소 하므로, 3으로 설정해야 다다음턴 동안 물고기가 안감.
            fish_count_array[move_x][move_y]=0


# 모든 칸을 검사하여 물고기 냄새가 존재하면 물고기 냄새를 1 감소 시키는 함수
def decrease_smell():
    for x in range(4):
        for y in range(4):
            if(fish_smell[x][y]>=1):
                fish_smell[x][y]-=1
                
# 복제된 물고기(copiedfish)를 배열(world)에 반영하는 함수          
def add_copiedfish_to_world(copiedfish,world):
    for x in range(4): 
        for y in range(4):
            world[x][y]+=copied_fish[x][y]

# 복제된 물고기 수를 기존의 물고기 수 배열에 반영하는 함수
def add_copiedfishcount_to_fish_count(copiedfish_count, fish_count):
    for x in range(4): 
        for y in range(4):
            fish_count[x][y]+=copied_fish_count[x][y]

#배열에 남아 있는 물고기의 수 반환하는 함수
def get_left_fish_count():
    return sum(sum(fish_count_array[i]) for i in range(4))
    
#main() 함수
    
start_fish_count, magic_practice_count=map(int,sys.stdin.readline().split())
world=[[[] for _ in range(4)] for _ in range(4)]
fish_count_array=[[0]*4 for _ in range(4)] # 각 칸에 있는 물고기 수를 담는 리스트

for _ in range(start_fish_count): # 초기 맵 설정
    x,y,direction=map(lambda x: int(x)-1,sys.stdin.readline().split())
    world[x][y].append(direction)
    fish_count_array[x][y]+=1
    
shark_position= list(map(lambda x: int(x)-1,sys.stdin.readline().split()))
fish_smell=[[0]*4 for _ in range(4)] # 물고기 냄새가 남아 있는 지를 담는 리스트

for _ in range(magic_practice_count):
    copied_fish=copy.deepcopy(world) # 1) 물고기 복제  
    copied_fish_count=copy.deepcopy(fish_count_array) # 복제된 물고기 수 임시 저장  
    all_fish_move() # 2) 모든 물고기 이동
    shark_move() # 3) 상어가 3칸 연속 움직임
    decrease_smell() #4) 모든 칸을 검사하여 물고기 냄새가 존재하면 물고기 냄새를 1 감소 시킨다.
    add_copiedfish_to_world(copied_fish,world) #5) 1에서 복제한 물고기를 world에 업데이트 시켜준다. 
    add_copiedfishcount_to_fish_count(copied_fish_count,fish_count_array) # 복제된 물고기 수 반영 

print(get_left_fish_count()) #남아 있는 물고기 수 (답)
