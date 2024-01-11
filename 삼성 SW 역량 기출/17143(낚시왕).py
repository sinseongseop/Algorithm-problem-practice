import sys

#구현, 시뮬레이션
# 삼성 SW 역량 기출
# 골드 1

dxdy=[(),(-1,0),(1,0),(0,1),(0,-1)] # X, 위, 아래 , 오른쪽, 왼쪽

# position 위치에서 땅에서 가장 가까운 상어를 낚시 한다.
def sharkFishing(position):
    global total_shark_size
    for i in range(R):
        if(world[i][position]!=[0,0,0]):
            total_shark_size+=world[i][position][2]            
            world[i][position]=[0,0,0]
            break
    
# 월드에 있는 모든 상어를 움직인다.            
def sharkMove():
    global world
    new_world=[[[0,0,0] for _ in range(C)] for _ in range(R)] # 모든 상어 이동 후 월드의 모습 
    for i in range(R):
        for j in range(C):
            if(world[i][j]!=[0,0,0]):
                shark_x=i
                shark_y=j
                shark_direction=world[i][j][1]
                shark_size=world[i][j][2]
                
                if(shark_direction==1 or shark_direction==2 ):
                    shark_speed=world[i][j][0]%(2*R-2)   
                    for _ in range(shark_speed):
                        if(shark_direction==2): # 상어 방향이 아래
                            if(shark_x!=R-1):
                                shark_x+=1
                            else: # 맨 아래에 있을 시 방향 바꿔야함
                                shark_x-=1
                                shark_direction=1                                
                        else: # 상어 방향이 위
                            if(shark_x!=0):
                                shark_x-=1
                            else: # 맨 위에 있을 시 방향 바꿔야함
                                shark_x+=1
                                shark_direction=2
                else:
                    shark_speed=world[i][j][0]%(2*C-2)
                    for _ in range(shark_speed):
                        if(shark_direction==4): # 상어 방향이 왼쪽
                            if(shark_y!=0): 
                                shark_y-=1
                            else: #상어가 맨 왼쪽에 도달시 방향 전환
                                shark_y+=1
                                shark_direction=3
                        else: # 상어 방향이 오른쪽
                            if(shark_y!=C-1):
                                shark_y+=1
                            else: # 상어가 맨 오른쪽에 도달시 방향 전환
                                shark_y-=1
                                shark_direction=4

                if(new_world[shark_x][shark_y][2]<shark_size): # 상어가 동일한 곳에 여러마리 존재 할 시 가장 큰 상어가 존재
                    new_world[shark_x][shark_y]=[shark_speed,shark_direction,shark_size]
                
    world=new_world # 업데이트 반영
                
# main() 함수

R,C,shark_count=map(int,sys.stdin.readline().split())
world=[[[0,0,0] for _ in range(C)] for _ in range(R)]


for _ in range(shark_count):
    x,y,speed,direction,size=map(int,sys.stdin.readline().split())
    world[x-1][y-1]=[speed,direction,size]


total_shark_size=0

for position in range(C):
    sharkFishing(position)
    sharkMove()

print(total_shark_size)