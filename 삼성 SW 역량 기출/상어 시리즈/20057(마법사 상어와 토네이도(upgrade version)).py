import sys
#구현, 시뮬레이션
# 삼성 SW 기출
#upgrade version
#골드 3

# 왼-1,아-1 // 오-2,위-2 // 왼-3,아-3 // 오-4, 위-4 // .... //오-N-1, 위- N-1 /// (특별항 왼 N-1 규칙(0,0에서 종료))

sand_rate=[[(5,0,-2),(10,1,-1),(10,-1,-1),(2,2,0),(7,1,0),(7,-1,0),(2,-2,0),(1,1,1),(1,-1,1)], 
           [(5,2,0),(10,1,1),(10,1,-1),(2,0,2),(7,0,1),(7,0,-1),(2,0,-2),(1,-1,1),(1,-1,-1)],
           [(5,0,2),(10,1,1),(10,-1,1),(2,2,0),(7,1,0),(7,-1,0),(2,-2,0),(1,1,-1),(1,-1,-1)],
           [(5,-2,0),(10,-1,1),(10,-1,-1),(2,0,2),(7,0,1),(7,0,-1),(2,0,-2),(1,1,1),(1,1,-1)]] # 왼쪽,아래,오른쪽 위로 이동할 때 위치 별 위치의 모래 비율 (실수 오차 의식해서 정수로 표현)

dxdy=[(0,-1),(1,0),(0,1),(-1,0)] # 왼쪽,아래쪽, 오른쪽, 위

# 토네이도가 1 cycle를 돌음 (왼,아래,오른쪽, 위 로 이동), 마지막 턴에는 왼쪽으로 이동 후 (0,0)에서 소멸
def move():
    global x,y,count

    for i in range(4): # 왼,아,오,위로 이동
    
        if(i==2): # 오른쪽과 위는 기존보다 한칸 더 많이 움직임
            count+=1
        
        move_dx, move_dy = dxdy[i]
        
        for j in range(count):
            x= x + move_dx
            y= y + move_dy
            if( world[x][y] != 0 ):
                total_move_sand = 0
                total_sand = world[x][y]
                world[x][y] = 0
                
                for rate, sand_dx, sand_dy in sand_rate[i]:
                    move_sand=total_sand*rate//100
                    if(0 <= x+sand_dx < N and 0 <= y+sand_dy < N):                    
                        world[x+sand_dx][y+sand_dy] += move_sand
                    total_move_sand += move_sand
                    
                if( 0 <= x+move_dx < N and 0 <= y+move_dy < N ):
                    world[x+move_dx][y+move_dy] += ( total_sand-total_move_sand )
            
            if(count==N and j==N-2): # 마지막은 특이항(0,0에서 토네이도 소멸)
                count+=1
                return
    
    count+=1

# 맵에 남아있는 모래의 총합을 반환하는 함수
def sum_sand():
    return sum(sum(row) for row in world)

#main()함수

N=int(sys.stdin.readline())

world=[]
for _ in range(N):
    world.append(list(map(int,sys.stdin.readline().split())))

x=N//2 # 시작 X값
y=N//2 # 시작 Y값
count=1 # 상어가 한 방향으로 움직이는 칸 수

initial_sand=sum_sand()

while(count<=N):
    move()

final_sand=sum_sand()
print(initial_sand-final_sand)
#print(world)