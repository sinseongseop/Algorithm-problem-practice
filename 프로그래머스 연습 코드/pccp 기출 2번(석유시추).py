from collections import deque

def solution(land):
    rowCnt = len(land)
    columnCnt = len(land[0])
    landNum=2 # 같은 석유 구역을 구분하는 인덱스, 0과 1은 이미 사용중이므로 2부터 순차적으로 석유 구역 구분
    oil = dict()
    for i in range(rowCnt):
        for j in range(columnCnt):
            if(land[i][j]==1):
                oilAmount = bfs(i,j,land,landNum, rowCnt, columnCnt)
                oil[landNum] = oilAmount
                landNum+=1
    
    #print(land, oil) #디버깅용
    
    answer = caluclateMaxOil(land, oil, rowCnt, columnCnt)
    return answer

dxdy=[(0,1), (1,0), (0,-1), (-1,0)]

def bfs(x, y, land, landNum, rowCnt, columnCnt):
    que=deque()
    que.append((x,y))
    land[x][y]=landNum

    areaSize=1
    
    while(que):
        x, y = que.popleft() 
        for dx, dy in dxdy:
            if(0<= x+dx< rowCnt and 0<= y+dy< columnCnt):
                if(land[x+dx][y+dy] == 1):
                    que.append((x+dx, y+dy))
                    land[x+dx][y+dy] = landNum
                    areaSize+=1
                    
    return areaSize

def caluclateMaxOil(land, oilAmount, rowCnt, columnCnt):
    maxOil=0

    for i in range(columnCnt):
        ignoreArea = set()
        ignoreArea.add(0)
        nowOil=0
            
        for j in range(rowCnt):
            if(land[j][i] not in ignoreArea):
                nowOil += oilAmount[land[j][i]]
                ignoreArea.add(land[j][i])
        maxOil = max(maxOil, nowOil)

    return maxOil

world=[[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]]
#world=[[1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1]]

print(solution(world))
