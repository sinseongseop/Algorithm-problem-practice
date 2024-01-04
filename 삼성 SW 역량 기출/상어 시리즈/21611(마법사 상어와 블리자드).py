import sys
from collections import deque
# 구현, 시뮬레이션
# 삼성 SW 기출
# 구현 매우 어려움.
# 2차원 자체 이용. 달팽이 수열을 1차원으로 바꿔서 풀 시 좀 더 쉽게 풀 수 있음.
# 골드1

magic_dxdy=[[],[-1,0],[1,0],[0,-1],[0,1]] # 사용안함, 위, 아래, 왼쪽, 오른쪽 순 
road_dxdy=[[0,-1],[1,0],[0,1],[-1,0]] #왼, 아 ,오 , 위 반복

# 방향, 거리를 입력받아 블리자드 마법을 수행하는 함수
def do_blizard_magic(magic_direction,distance):
    x=N//2
    y=N//2
    dx,dy=magic_dxdy[magic_direction]
    for _ in range(distance):
        x=x+dx
        y=y+dy
        if(0<=x<N and 0<=y<N):
            world[x][y]=0
        else:
            break

# 중간에 빈칸이 존재하면 빈칸을 없애는 함수
def remove_blank():
    global world
    new_world=[[0]*N for _ in range(N)]
    # 기존 맵을 가리키는 위치
    world_x=N//2
    world_y=N//2
    # 구슬이 위치할 위치
    new_world_x=N//2
    new_world_y=N//2
    new_world_level=1
    new_world_count=0
    new_world_direction=0
   
    count=0
    for repeat in range(N//2+1):
        for i in range(4): # 왼,아,오,위 반복
            # 왼쪽으로 갈때는 위로 갈때보다 1칸 더 많이 움직임
            # 오른쪽으로 갈때는 아래로 갈때보다 1칸 더 많이 움직이므로
            if((i==0 or i==2) and (repeat!=N//2)): 
                count+=1
            
            dx,dy=road_dxdy[i]
            for _ in range(count):
                world_x+=dx
                world_y+=dy
                
                if(world[world_x][world_y]!=0):
                    new_dx,new_dy=road_dxdy[new_world_direction%4]
                    new_world_x+=new_dx
                    new_world_y+=new_dy
                    new_world_count+=1
                    new_world[new_world_x][new_world_y]=world[world_x][world_y]
                    if(new_world_count==new_world_level):
                        new_world_count=0
                        new_world_direction+=1
                        if(new_world_direction%2==0):
                            new_world_level+=1         
            
            if(world_x==0 and world_y==0):
                break
        
    world=new_world # 바뀐 맵으로 업데이트 시켜 주기

# 구슬이 폭발 해야 하는 위치를 모두 찾는 함수
def find_explosion_position():
    remove_position=[] # 폭발하는 구슬의 시작과 종료 위치를 저장하는 리스트
    x=N//2
    y=N//2
    count=0
    marble_count=0
    start=[N//2,N//2]
    now_num=0
    for repeat in range(N//2+1):
        for i in range(4):
            if((i==0 or i==2) and (repeat!=N//2)):        
                count+=1
            
            dx,dy=road_dxdy[i]
            
            for _ in range(count):
                x=x+dx
                y=y+dy
                if(now_num!=0):
                    if(world[x][y]==now_num): # 이전 구슬과 번호가 같은 경우
                        marble_count+=1
                    else:
                        if(marble_count>=4): # 동일한 번호가 4개 이상 나오는 경우(폭발 대상)
                            remove_position.append([start,[x,y]]) # start는 포함 ~ [x,y]는 미포함 
                        start=[x,y]
                        marble_count=1
                        now_num=world[x][y]
                else: 
                    if(world[x][y]!=0):
                        start=[x,y]
                        marble_count=1
                        now_num=world[x][y]
            
            if(x==0 and y==0):
                break
    
    return remove_position
            
#구슬 폭발을 실행하는 함수
def marble_explosion():
    global explosion_count_one,explosion_count_two,explosion_count_three

    is_explosion=False #폭발 발생 여부 플래그
    
    remove_position=find_explosion_position() # 폭발의 모든 위치를 찾는다.
    
    count=0
    direction=0
    level=1
    x=N//2
    y=N//2
    
    for start,end in remove_position:     
        is_explosion=True
        is_remove=False
        remove_num=-1
        while([x,y]!=end):
            
            if([x,y]==start):
                is_remove=True
                remove_num=world[x][y]
            
            if(is_remove):
                world[x][y]=0
                if(remove_num==1):
                    explosion_count_one+=1
                elif(remove_num==2):
                    explosion_count_two+=1
                elif(remove_num==3):
                    explosion_count_three+=1
                    
            dx,dy=road_dxdy[direction%4]
            x+=dx
            y+=dy
            count+=1
            if(count==level):
                count=0
                direction+=1
                if(direction%2==0):
                    level+=1
  
    return is_explosion

# 구슬을 변환하는 함수
def change_marble():
    global world
    new_world=[[0]*N for _ in range(N)]
    # 기존 맵을 가리키는 위치
    world_x=N//2
    world_y=N//2
    # 구슬이 위치할 위치
    new_world_x=N//2
    new_world_y=N//2
    new_world_level=1
    new_world_count=0
    new_world_direction=0
    
    marble_num=world[N//2][N//2-1] 
    marble_count=0
   
    count=0
    for repeat in range(N//2+1):
        for i in range(4): # 왼,아,오,위 반복
            # 왼쪽으로 갈때는 위로 갈때보다 1칸 더 많이 움직임
            # 오른쪽으로 갈때는 아래로 갈때보다 1칸 더 많이 움직이므로
            if((i==0 or i==2) and (repeat!=N//2)): 
                count+=1
            
            dx,dy=road_dxdy[i]
            for _ in range(count):
                world_x+=dx
                world_y+=dy
                
                if(marble_num==world[world_x][world_y]):
                    marble_count+=1
                else:
                    for j in range(2):
                        new_dx,new_dy=road_dxdy[new_world_direction%4]
                        new_world_x+=new_dx
                        new_world_y+=new_dy
                        new_world_count+=1
                        if(j==0):
                            new_world[new_world_x][new_world_y]=marble_count
                        else:
                            new_world[new_world_x][new_world_y]=marble_num
                        
                        if(new_world_count==new_world_level):
                            new_world_count=0
                            new_world_direction+=1
                            if(new_world_direction%2==0):
                                new_world_level+=1   

                    marble_count=1
                    marble_num=world[world_x][world_y]
                    
                if(new_world_x==0 and new_world_y==0):
                    break    
            
            if((world_x==0 and world_y==0) or(new_world_x==0 and new_world_y==0) ):
                break
        
        if((world_x==0 and world_y==0) or(new_world_x==0 and new_world_y==0) ):
            break
    
    if(not(new_world_x==0 and new_world_y==0) and marble_num!=0 ):
        for i in range(2):
            new_dx,new_dy=road_dxdy[new_world_direction%4]
            new_world_x+=new_dx
            new_world_y+=new_dy
            new_world_count+=1
            if(i==0):
                new_world[new_world_x][new_world_y]=marble_count
            else:
                new_world[new_world_x][new_world_y]=marble_num
            
            if(new_world_count==new_world_level):
                new_world_count=0
                new_world_direction+=1
                if(new_world_direction%2==0):
                    new_world_level+=1   

        marble_count=1
        marble_num=world[world_x][world_y]
        
    world=new_world # 바뀐 맵으로 업데이트 시켜 주기

# main() 함수

N,magic_count=map(int,sys.stdin.readline().split())
world=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
explosion_count_one=0 #1번 구슬 폭발 총 개수
explosion_count_two=0 #2번 구슬 폭발 총 개수
explosion_count_three=0 #3번 구슬 폭발 총 개수

for _ in range(magic_count):
    magic_direction,distance=map(int,sys.stdin.readline().split()) # 0) 마법 방향과 거리를 입력 받음
    do_blizard_magic(magic_direction,distance) # 1) 마법을 수행함
    is_explosion=True  #폭발 헀는 가?   
    while(is_explosion): 
        remove_blank() #2) 빈칸 제거
        is_explosion=marble_explosion() #3) 구슬 폭발을 진행하고, 폭발이 발생하면 True를 반환    

    change_marble() # 4) 구슬을 변환 규칙에 따라 변환

print(explosion_count_one+2*explosion_count_two+3*explosion_count_three)