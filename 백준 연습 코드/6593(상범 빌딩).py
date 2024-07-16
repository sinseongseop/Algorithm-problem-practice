import sys
from collections import deque
# 그래프 탐색 , BFS
# 골드 5

dxdydz=[(1,0,0),(0,1,0),(0,0,1),(-1,0,0),(0,-1,0),(0,0,-1)]

def findRoad(start, destination):
    global world, visited, floorCnt, rowCnt, columnCnt
    
    que=deque()
    que.append((start[0],start[1],start[2],0))
    
    while(que):
        (x,y,z,moveCnt) = que.popleft()
        
        #탈출 하는 경우
        if( (x,y,z) == destination ):
            print("Escaped in ", end="") 
            print(moveCnt, end="") 
            print(" minute(s).")          
            return   

        for dx,dy,dz in dxdydz:
            if( (0 <= x+dx < floorCnt) and (0 <= y+dy < rowCnt) and (0 <= z+dz < columnCnt)
               and ( world[x+dx][y+dy][z+dz] == "." or world[x+dx][y+dy][z+dz] == "E")
               and visited[x+dx][y+dy][z+dz] == False ):
                que.append((x+dx,y+dy,z+dz,moveCnt+1))
                visited[x+dx][y+dy][z+dz]=True


    #탈출 불가능인 경우
    print("Trapped!")
    

# main()
while(True):
    floorCnt, rowCnt, columnCnt = map(int,sys.stdin.readline().split())
    startPostion=0
    destinationPosition=0
      
    # 종료 조건
    if((floorCnt,rowCnt,columnCnt) == (0,0,0)):
        break
    
    # 월드, 방문 초기화
    world = []
    for _ in range(floorCnt):
        floorMap = []
        for _ in range(rowCnt):
            floorMap.append(sys.stdin.readline().strip())        
        world.append(floorMap)
        sys.stdin.readline() # 층 구분을 위한 공백
    
    visited=[[[False]*columnCnt for _ in range(rowCnt)] for _ in range(floorCnt)]
    
    # 시작, 종료 지점 찾기
    for floor in range(floorCnt):
        for row in range(rowCnt):
            for column in range(columnCnt):
                if(world[floor][row][column] == "S"):
                    startPostion=(floor,row,column)
                if(world[floor][row][column] == "E"):
                    destinationPosition=(floor,row,column)
    
    # 길 찾기
    findRoad(startPostion, destinationPosition)
    
    #print(visited) #디버깅용