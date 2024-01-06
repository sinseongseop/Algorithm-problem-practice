import sys
#구현,시뮬레이션
#플래 5

# 물고기가 가장 작은 어항에 물고기 1마리씩 추가해 주는 함수
def insert_fish_in_smallests():
    min_fish=10**6
    min_position=[]
    for i in range(N):
        if( min_fish> world[0][i]):
            min_fish=world[0][i]
            min_position=[i]
        elif(min_fish == world[0][i]):
            min_position.append(i)
    
    for i in min_position:
        world[0][i]+=1

# 가장 왼쪽 어항을 오른쪽 어항 위에 쌓는 함수
def move_left_most_bowl():
    world[1][1]=world[0][0]
    world[0][0]=0

#2개 이상의 어항이 있는 경우 90도를 회전하여 어항 위에 쌓는 함수
def rotate_90():
    i=0
    j=0
    while(world[i][j]==0):
        j+=1
    
    # 옮겨야 하는 덩어리의 왼쪽 아래 모서리 좌표
    left_x=i 
    left_y=j
    
    while(i<N and world[i][j]):
        i+=1
    
    i-=1
    while(j<N and world[i][j]):
        j+=1
    j-=1
    
    # 옮겨야하는 덩어리의 오른쪽 위 모서리 좌표
    right_x=i
    right_y=j
    
    if(right_x+j+1>=N):
        return False
    else:
        world_x=0
        move_y=right_y+1
        
        for _ in range(right_y-left_y+1):
            world_x+=1
            world_y=j
            move_x = (-1)
            move_y -= 1
            
            for _ in range(right_x-left_x+1):
                 world_y+=1
                 move_x+=1
                 world[world_x][world_y]=world[move_x][move_y]
                 world[move_x][move_y]=0
                
        return True
        
# 인접한 어항의 물고기를 조건에 맞게 움직인다.
def move_fishes():   
    bowl_change_count=[[0]*N for _ in range(N)] # 각 어항마다 변동되는 물고기 수
    
    for i in range(N):
        for j in range(N):
            if(j+1<N and world[i][j]!=0 and world[i][j+1]!=0):
                move_fish=abs(world[i][j]-world[i][j+1])//5
                if(world[i][j]>world[i][j+1]):
                    bowl_change_count[i][j]-=move_fish
                    bowl_change_count[i][j+1]+=move_fish
                else:
                    bowl_change_count[i][j]+=move_fish
                    bowl_change_count[i][j+1]-=move_fish
            
            if(i+1<N and world[i][j]!=0 and world[i+1][j]!=0):
                move_fish=abs(world[i+1][j]-world[i][j])//5
                if(world[i+1][j]>world[i][j]):
                    bowl_change_count[i+1][j]-=move_fish
                    bowl_change_count[i][j]+=move_fish
                else:
                    bowl_change_count[i+1][j]+=move_fish
                    bowl_change_count[i][j]-=move_fish        

    for i in range(N):
        for j in range(N):
            world[i][j]+=bowl_change_count[i][j]

#어항을 일자로 편다
def make_bowl_line():
    global world
    new_world=[[0]*N for _ in range(N)]
    new_position=0
    for y in range(N):
        for x in range(N):
            if(world[x][y]!=0):
                new_world[0][new_position]=world[x][y]
                new_position+=1
            else:
                break
    
    world=new_world  

#start_x~ end_x까지의 어항을 180도 회전 시킨다. (level=1 이면 첫번째 수행, level=2면 두번째 수행)
def half_rotate_180(start_y,end_y,level): 
    for y in range(end_y-(end_y-start_y)//2-1,start_y-1,-1):
        for x in range(level-1,-1,-1):
            #print(x,y,(2*level-1)-x,start_y+(end_y-y))
            world[(2*level-1)-x][start_y+(end_y-y)]=world[x][y]
            world[x][y]=0

#어항에 있는 물고기의 최대치- 최소치를 반환한다.
def get_max_min_difference():
    max_fish=-1
    min_fish=10**5
    for i in range(N):
        for j in range(N):
            if(world[i][j]!=0):
                max_fish=max(max_fish,world[i][j])
                min_fish=min(min_fish,world[i][j])

    return max_fish-min_fish

# main() 함수

N,K=map(int,sys.stdin.readline().split())
world=[[0]*N for _ in range(N)]

fishes=list(map(int,sys.stdin.readline().split()))

for i in range(N):
    world[0][i]=fishes[i]


repeat_count=0 # 반복횟수(답안)
Max_min_difference=10**5

while(Max_min_difference>K): # 어항에 있는 물고기의 최대-최소가 K 마리가 될때까지 반복
    repeat_count+=1
    insert_fish_in_smallests() # 1) 물고기가 가장 작은 어항에 물고기를 1마리 추가한다.
    move_left_most_bowl() # 2) 가장 왼쪽에 있는 어항을 옮긴다.
    rotate_flag=True
    while(rotate_flag): # 3) 2개 이상의 어항이 수직으로 쌓여 있으면 조건에 맞게 어항을 옮긴다.
        rotate_flag=rotate_90()
    move_fishes() # 4) 인접한 어항끼리 동시에 조건에 맞게 물고기를 이동시킨다.
    make_bowl_line() # 5) 어항을 일직선으로 편다
    half_rotate_180(0,N-1,1) # 6-1) 절반 180도 회전 1번 수행 
    half_rotate_180(N//2,N-1,2) #6-2) 절반 180도 회전 1번 더 수행
    move_fishes() # 7) 물고기를 이동 시킨다.
    make_bowl_line() # 8) 어항을 일직선으로 편다
    Max_min_difference=get_max_min_difference()

#print(world)
print(repeat_count)