import sys
# 구현
#삼성 SW 역량 기출
#골드5

dxdy=[(-1,0),(0,1),(1,0),(0,-1)]

N=int(sys.stdin.readline())
world=[[-1]*N for _ in range(N)] # -1은 학생이 배정되지 않은 빈칸을 의미

like=[0 for _ in range(N*N)]

for _ in range(N*N):
    people=list(map(lambda x : int(x)-1,sys.stdin.readline().split()))
    like[people[0]]=people[1:]
    
    sit_people=people[0] #이번에 앉는 사람 번호
    
    sit_position_x=-1 # 앉는 위치의 x값
    sit_position_y=-1 # 앉는 위치의 y값
    now_near_like=-1 # 앉는 위치에서 인접한 좋아하는 사람 수
    now_near_blank=-1 # 앉는 위치에서 인접한 빈칸 수
    
    for x in range(N):
        for y in range(N):
            if(world[x][y]==-1):
                near_like=0 # 인접한 좋아하는 사람 수
                near_blank=0 # 인접한 빈칸 수
                for dx,dy in dxdy:
                    if(0<=x+dx<N and 0<=y+dy<N):
                        if(world[x+dx][y+dy] in like[sit_people]):
                            near_like+=1
                        elif(world[x+dx][y+dy]==-1):
                            near_blank+=1
                    
                # 우선 순위에 맞게 자리 배정 위치 업데이트    
                if(near_like>now_near_like):  # 1순위) 좋아하는 사람이 많은 곳
                    now_near_like=near_like
                    now_near_blank=near_blank
                    sit_position_x=x
                    sit_position_y=y
                elif(near_like==now_near_like and near_blank>now_near_blank): # 2순위) 주변에 빈공간이 많은 곳
                    now_near_blank=near_blank
                    sit_position_x=x
                    sit_position_y=y
    
    world[sit_position_x][sit_position_y]=sit_people # 자리 배정 확정
    #print(world) #디버깅 확인용

#print(world)

# 학생 만족도의 총합 구하기
answer=0

for x in range(N):
    for y in range(N):
        like_count=0
        for dx,dy in dxdy:
            if(0<=x+dx<N and 0<=y+dy<N and world[x+dx][y+dy] in like[world[x][y]]):
                like_count+=1

        if(like_count>=1):    
            answer+=(10**(like_count-1))

print(answer)
        