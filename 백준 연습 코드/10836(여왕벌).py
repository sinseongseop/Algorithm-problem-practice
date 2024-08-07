import sys

# 구현, 시뮬레이션
# 골드 3

# 애벌레의 크기는 왼쪽, 왼쪽 위, 위쪽 하나의 크기로만 변하고, 
# 애벌레의 크기 증가가 정렬된 상태로 주어지므로 모든 칸을 계산 할 필요가 없다.

M, day = map(int, sys.stdin.readline().split())

larvaSize = [1]*(2*M-1)

for _ in range(day):
    cntPerChange = list(map(int, sys.stdin.readline().split()))
    larvaNum = 0
    
    #각 애벌레의 크기를 변경
    for i in range(3):
        count = cntPerChange[i]
        while(count > 0):
            larvaSize[larvaNum] += i
            count -= 1
            larvaNum += 1

larvaMatrix = [[0]*M for _ in range(M)]
row= M-1
column = 0

for i in range(2*M-1):
    size = larvaSize[i]
    if( row == 0  and column!= 0):
        for j in range(0,M):
            larvaMatrix[j][column] = size
        column +=1
    elif (row == 0 and column == 0):
        larvaMatrix[row][column] = size
        column +=1
    
    else:
        larvaMatrix[row][0] = size
        row -= 1


# 답 출력
for i in range(M):
    for j in range(M):
        print(larvaMatrix[i][j], end = ' ')
    print()