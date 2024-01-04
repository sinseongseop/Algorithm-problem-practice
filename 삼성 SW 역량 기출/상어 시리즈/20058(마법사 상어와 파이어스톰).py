import sys
import copy
from collections import deque
#구현, 시뮬레이션, 그래프 탐색 , BFS
#삼성 SW 기출
# 골드3
#python3 로 제출시 시간초과, pypy3으로는 가능 


# matrix 행렬의 (x,y)에 해당한는 부분이 들어있는 2^length*2^length 파트를 시계방향으로 90도 회전시키는 함수 
def one_part_rotate90_clockwise(matrix,x,y,length):
    result_matrix=[[0]*length for _ in range(length)]
    for i in range(x,x+length):
        for j in range(y,y+length):
            result_matrix[j-y][length-1-i+x]=matrix[i][j]
    
    for i in range(x,x+length):
        for j in range(y,y+length):
            matrix[i][j]=result_matrix[i-x][j-y]

# matrix 행렬의 모든 파트를 2^length*2^length 로 쪼개서 시계방향으로 90도 회전시키는 함수
def all_part_rotate90_clockwise(matrix,length):
    for i in range(0,matrix_size,length):
        for j in range(0,matrix_size,length):
            one_part_rotate90_clockwise(matrix,i,j,length)

dxdy=[[-1,0],[0,1],[1,0],[0,-1]]

# 모든 칸을 탐색하며 인접 얼음이 2개이하인 경우 그 칸을 얼음을 1 감소시키고, 그 결과로 나온 행렬을 반환하는 함수
def return_melt_ice_world(world):
    result_matrix=copy.deepcopy(world)
    for x in range(matrix_size):
        for y in range(matrix_size):
            if(world[x][y]!=0): # 얼음이 존재하면
                near_ice_count=0
                for dx,dy in dxdy:
                    if(0<=x+dx<matrix_size and 0<=y+dy<matrix_size and world[x+dx][y+dy]!=0 ):
                        near_ice_count+=1
                if(near_ice_count<3): # 인접 얼음이 2개 이하인 경우 1 감소
                    result_matrix[x][y]-=1
    
    world=result_matrix  
    return world          

# x,y와 서로 연결되어 있는 얼음의 개수를 반환하는 함수 (BFS 이용)
def return_meet_ice_count(x,y,visited):
    que=deque()
    que.append([x,y])
    visited[x][y]=True
    meet_count=0
    while(que):
        x,y=que.pop()
        meet_count+=1
        for dx,dy in dxdy:
            if(0<=x+dx<matrix_size and 0<=y+dy<matrix_size and world[x+dx][y+dy]!=0 and visited[x+dx][y+dy]==False): 
                que.append([x+dx,y+dy])
                visited[x+dx][y+dy]=True
    
    return meet_count

# main() 함수
  
N,Q=map(int,sys.stdin.readline().split())
matrix_size=2**N # 행렬의 한변의 길이
world=[list(map(int,sys.stdin.readline().split())) for _ in range(matrix_size)]
request_order=list(map(int,sys.stdin.readline().split()))

#print(world)
for request_level in request_order:
    all_part_rotate90_clockwise(world,2**request_level)
    world=return_melt_ice_world(world)
    #print(world)

total_ice=0 # 총 얼음 개수
max_meet_ice=0 # 최대 얼음 덩어리
visited=[[False]*matrix_size for _ in range(matrix_size)]

for i in range(matrix_size):
    for j in range(matrix_size):
        if(world[i][j]!=0):
            total_ice+=world[i][j] 
            if(visited[i][j]==False):
                meet_ice=return_meet_ice_count(i,j,visited)
                max_meet_ice=max(meet_ice,max_meet_ice)

print(total_ice)
print(max_meet_ice)
