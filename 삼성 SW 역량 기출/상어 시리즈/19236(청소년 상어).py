import sys
import copy

# 구현, DFS, 시뮬레이션
# 삼성 SW 역량 테스트 기출
# 실수 할 부분 많음. 실수 주의!!
# 골드 2

world=[]
for _ in range(4):
    line=list(map(int,sys.stdin.readline().split()))
    line_arr=[]
    for i in range(0,8,2):
        line_arr.append([line[i],line[i+1]])
    world.append(line_arr)

move_direction=[[-1,0],[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1]] # 상어랑 물고기가 이동하는 방향

def update_world(world): # 물고기의 움직임을 업데이트 해준다.
    for i in range(1,17):
        find_flag=False # i 번째 물고기를 찾았나?
        for j in range(0,4):
            for k in range(0,4):
                if(world[j][k][0]==i): # i번째 물고기 이면
                    for m in range(world[j][k][1]-1, world[j][k][1]-1+8,1): # 45도씩 돌리며 물고기가 갈 수 있는  최초의 방향 확인
                        #print(move_direction[m%8]) #디버깅 용
                        move_x,move_y = move_direction[m%8] #물고기가 움직이는 방향
                        if(0<=j+move_x<4 and 0<=k+move_y<4 and world[j+move_x][k+move_y][0]!=-1): # 물고기가 갈 수 있는 곳이면
                            world[j][k][1]=m%8+1 # 물고기 고유 방향을 물고기가 움직이는 방향으로 업데이트
                            world[j][k],world[j+move_x][k+move_y]=world[j+move_x][k+move_y], world[j][k] # Swap
                            find_flag=True # 찾았으니까 falg=True
                            break
                if(find_flag):
                    break
            if(find_flag):
                break


def DFS(world,shark_position,shark_point,shark_direction): # 상어가 움직일 수 있는 모든 경로 탐색
    global Max_point
    stack=[[world,shark_position,shark_point,shark_direction]]
    while(stack):
        world,shark_position,shark_point,shark_direction=stack.pop()
        Max_point=max(Max_point,shark_point)
        
        x,y=shark_position # 상어의 현 위치
        dx,dy=move_direction[shark_direction] #상어가 움직이는 방향
        for i in range(1,4):
            if(0<=x+i*dx<4 and 0<=y+i*dy<4 and world[x+i*dx][y+i*dy][0]!=0): # 빈 공간으로는 상어가 못 감
                new_world=copy.deepcopy(world) # 3차원 배열을 전부 복사해야하므로 Deep copy 사용.
                new_world[x][y]=[0,0] # 기존에 상어가 있던 위치는 0,0으로 변경
                new_shark_position=[x+i*dx,y+i*dy] #새로운 상어 위치 계산
                new_point=shark_point+new_world[x+i*dx][y+i*dy][0] # 점수 업데이트
                new_shark_direction=new_world[x+i*dx][y+i*dy][1]-1 # 상어가 가지는 방향 업데이트
                new_world[x+i*dx][y+i*dy]=[-1,0] # 맵에 새로운 상어 위치 표시
                update_world(new_world) # 물고기 움직임 업데이트
                stack.append([new_world,new_shark_position,new_point,new_shark_direction])
 
# main() 함수

Max_point=0 # 최대 점수 (답)

shark_point=world[0][0][0] # 초기 점수
shark_direction=world[0][0][1]-1 # 초기 상어 방향
shark_position=[0,0] # 초기 상어 위치

world[0][0]=[-1,0]  # 상어가 있는 위치는 -1로 표현

#print(world)
update_world(world) # 초기 물고기 움직임 업데이트
#print(world)
DFS(world,shark_position,shark_point,shark_direction) #DFS 탐색
print(Max_point)