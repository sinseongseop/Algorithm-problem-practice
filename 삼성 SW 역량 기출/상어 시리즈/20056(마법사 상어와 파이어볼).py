import sys
import copy
# 구현, 시뮬레이션
# 삼성 sw 기출
# 골드 4

dxdy=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

# 모든 파이어볼을 움직이는 함수
def move_fireball(): 
    global world,fire_ballcount
    new_world=[[[0, 0, 0] for _ in range(N)] for _ in range(N)] # 움직인 후 파이어 볼의 상태
    fire_ballcount=[[0]*N for _ in range(N)] # 각 칸 마다 몇개의 파이어 볼이 있는가
    for x in range(N):
        for y in range(N):
            if(world[x][y][0]!=0): # 파이어 볼이 존재 하면
                if(world[x][y][2]>=0): # 공이 하나만 존재 하는 경우
                    dx,dy=dxdy[world[x][y][2]]
                    speed=world[x][y][1]
                    new_x=(x+dx*speed)%N
                    new_y=(y+dy*speed)%N
                    if(new_world[new_x][new_y][0]==0): #  빈칸으로 가는 경우
                        new_world[new_x][new_y]=copy.deepcopy(world[x][y])
                    else: 
                        if(((new_world[new_x][new_y][2]>=0 and new_world[new_x][new_y][2]%2==1) or new_world[new_x][new_y][2]==-1)  and world[x][y][2]%2==1): # 홀수 방향만 존재
                            new_world[new_x][new_y]=[new_world[new_x][new_y][0]+world[x][y][0],new_world[new_x][new_y][1]+world[x][y][1],-1]
                        elif(((new_world[new_x][new_y][2]>=0 and new_world[new_x][new_y][2]%2==0) or new_world[new_x][new_y][2]==-2) and world[x][y][2]%2==0): # 짝수 방향만 존재
                            new_world[new_x][new_y]=[new_world[new_x][new_y][0]+world[x][y][0],new_world[new_x][new_y][1]+world[x][y][1],-2]
                        else: # 홀수,짝수 혼합
                            new_world[new_x][new_y]=[new_world[new_x][new_y][0]+world[x][y][0],new_world[new_x][new_y][1]+world[x][y][1],-3]
                    fire_ballcount[new_x][new_y]+=1
                else: # 공이 분해되어 4개 존재하는 경우 (4방향으로 움직임)
                    if(world[x][y][2]==-1 or world[x][y][2]==-2): # 방향이 다 홀수 or 다 짝수 인 경우 (0,2,4,6 방향으로 날아감)
                        for i in range(0,8,2):
                            dx,dy=dxdy[i]
                            speed=world[x][y][1]
                            new_x=(x+dx*speed)%N
                            new_y=(y+dy*speed)%N
                            if(new_world[new_x][new_y][0]==0): # 빈칸 도착 하는 경우
                                new_world[new_x][new_y]=[world[x][y][0],world[x][y][1],i]
                            else: # 움직인 칸에 다른 파이어 볼이 존재하는 경우
                                if((new_world[new_x][new_y][2]>=0 and new_world[new_x][new_y][2]%2==0) or new_world[new_x][new_y][2]==-2): # 다 짝수 인 경우
                                    new_world[new_x][new_y]=[new_world[new_x][new_y][0]+world[x][y][0],new_world[new_x][new_y][1]+world[x][y][1],-2]
                                else: 
                                    new_world[new_x][new_y]=[new_world[new_x][new_y][0]+world[x][y][0],new_world[new_x][new_y][1]+world[x][y][1],-3]          
                            fire_ballcount[new_x][new_y]+=1
                    else: # 그외 (1,3,5,7 방향으로 날아감)
                        for i in range(1,8,2):
                            dx,dy=dxdy[i]
                            speed=world[x][y][1]
                            new_x=(x+dx*speed)%N
                            new_y=(y+dy*speed)%N
                            if(new_world[new_x][new_y][0]==0): # 빈칸 도착 하는 경우
                                new_world[new_x][new_y]=[world[x][y][0],world[x][y][1],i]
                            else: # 다른 파이어 볼이 존재 하는 경우
                                if((new_world[new_x][new_y][2]>=0 and new_world[new_x][new_y][2]%2==1) or new_world[new_x][new_y][2]==-1): # 다 홀수 이면
                                    new_world[new_x][new_y]=[new_world[new_x][new_y][0]+world[x][y][0],new_world[new_x][new_y][1]+world[x][y][1],-1]
                                else:
                                    new_world[new_x][new_y]=[new_world[new_x][new_y][0]+world[x][y][0],new_world[new_x][new_y][1]+world[x][y][1],-3]          
   
                            fire_ballcount[new_x][new_y]+=1
    world=new_world # 월드를 새로운 상태로 업데이트

 # 합쳐진 파이어 볼을 분해 하는 함수
def decomposite_fireball():
    global world,fire_ballcount
    for i in range(N):
        for j in range(N):
            if(world[i][j][2]<0):
                world[i][j][0]=world[i][j][0]//5
                world[i][j][1]=world[i][j][1]//fire_ballcount[i][j]
                if(world[i][j][0]==0):
                    world[i][j]=[0,0,0]
                    
# 존재하는 모든 파이어볼의 질량을 더한 값을 보여 주는 함수
def sum_fireball_mass(): 
    global world
    total=0
    for i in range(N):
        for j in range(N):
            if(world[i][j][2]<0): # 동일한 질량을 가진 공이 한 칸에 4개 존재하는 상황
                total+=world[i][j][0]*4
            else:
                total+=world[i][j][0]
    
    return total

# main() 함수

N,M,K=map(int,sys.stdin.readline().split())

world=[[[0, 0, 0] for _ in range(N)] for _ in range(N)]

for _ in range(M): # 초기 상태 설정
    x,y,mass,speed,direction=map(int,sys.stdin.readline().split())
    world[x-1][y-1]=[mass,speed,direction]

fire_ballcount=[]

for _ in range(K): # K번 동안 볼 움직이기, 볼 분해하기 반복
    move_fireball()
    decomposite_fireball()

print(sum_fireball_mass()) # 파이어볼의 질량합 출력


