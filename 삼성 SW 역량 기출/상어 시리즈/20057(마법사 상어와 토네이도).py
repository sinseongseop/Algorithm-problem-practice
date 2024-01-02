import sys
#구현, 시뮬레이션
# 삼성 SW 기출
#골드 3

# 왼-1,아-1 // 오-2,위-2 // 왼-3,아-3 // 오-4, 위-4 // .... //오-N-1, 위- N-1 /// (특별항 왼 N-1 규칙(0,0에서 종료))

sand_rate=[(5,0,-2),(10,1,-1),(10,-1,-1),(2,2,0),(7,1,0),(7,-1,0),(2,-2,0),(1,1,1),(1,-1,1)] # 상대적 위치의 모래 비율 (실수 오차 의식해서 정수로 표현)

# 토네이도가 count 횟수만큼 왼쪽으로 이동
def left_move(count):
    global x,y

    for i in range(count):
        y=y-1
        if(world[x][y]!=0):
            total_move_sand=0
            total_sand=world[x][y]
            world[x][y]=0
            
            for rate,dx,dy in sand_rate:
                move_sand=total_sand*rate//100
                if(0<=x+dx<N and 0<=y+dy<N):                    
                    world[x+dx][y+dy]+= move_sand
                total_move_sand+=move_sand
                
            if(0<=y-1<N):
                world[x][y-1]+=(total_sand-total_move_sand)

# 토네이도가 count 횟수만큼 아래로 이동
def down_move(count):
    global x,y

    for _ in range(count):
        x=x+1
    
        if(world[x][y]!=0):
            total_move_sand=0
            total_sand=world[x][y]
            world[x][y]=0
            
            for rate,dy,dx in sand_rate:
                dx=-dx
                move_sand=total_sand*rate//100
                if(0<=x+dx<N and 0<=y+dy<N):
                    world[x+dx][y+dy]+=move_sand
            
                total_move_sand+=move_sand
                    
            if(0<=x+1<N):
                world[x+1][y]+=(total_sand-total_move_sand)

# 토네이도가 count 횟수만큼 오른쪽으로 이동
def right_move(count):
    global x,y

    for _ in range(count):
        y=y+1
        if(world[x][y]!=0):
            total_move_sand=0
            total_sand=world[x][y]
            world[x][y]=0
            
            for rate,dx,dy in sand_rate:
                dy=-dy
                move_sand=total_sand*rate//100
                if(0<=x+dx<N and 0<=y+dy<N):                    
                    world[x+dx][y+dy]+= move_sand
                total_move_sand+=move_sand
                
            if(0<=y+1<N):
                world[x][y+1]+=(total_sand-total_move_sand)

# 토네이도가 count 횟수만큼 위로 이동          
def up_move(count):
    global x,y

    for _ in range(count):
        x=x-1
    
        if(world[x][y]!=0):
            total_move_sand=0
            total_sand=world[x][y]
            world[x][y]=0
            
            for rate,dy,dx in sand_rate:
                move_sand=total_sand*rate//100
                if(0<=x+dx<N and 0<=y+dy<N):
                    world[x+dx][y+dy]+=move_sand
            
                total_move_sand+=move_sand
                    
            if(0<=x-1<N):
                world[x-1][y]+=(total_sand-total_move_sand)

# 맵에 남아있는 모래의 총합을 반환하는 함수
def sum_sand():
    total=0
    for i in range(N):
        for j in range(N):
            total+=world[i][j]
    return total

#main()함수

N=int(sys.stdin.readline())

world=[]
for _ in range(N):
    world.append(list(map(int,sys.stdin.readline().split())))

x=N//2 # 시작 X값
y=N//2 # 시작 Y값
count=1 # 상어가 한 방향으로 움직이는 칸 수

initial_sand=sum_sand()

while(count<N):
    left_move(count)
    down_move(count)
    count+=1
    right_move(count)
    up_move(count)
    count+=1

left_move(count-1)
final_sand=sum_sand()
print(initial_sand-final_sand)
print(world)