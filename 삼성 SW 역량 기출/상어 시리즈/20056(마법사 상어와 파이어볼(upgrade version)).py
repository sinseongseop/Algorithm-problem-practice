import sys

# 구현, 시뮬레이션
# 삼성 sw 기출
# 골드 4
#upgrade version

N,M,K = map(int, sys.stdin.readline().split())

fireballs = [] # 모든 파이어 볼 정보를 담을 리스트

for _ in range(M): #초기 파이어 볼 정보 저장
    x,y,mass,speed,direction=list(map(int, sys.stdin.readline().split()))
    fireballs.append([x,y,mass,speed,direction])

world=[[[] for _ in range(N)] for _ in range(N)]

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

for _ in range(K):
    # 파이어볼 이동
    while fireballs:
        x, y, mass, speed, direction = fireballs.pop()
        new_x = (x + speed * dx[direction]) % N  # 1번과 N 번 행 연결
        new_y = (y + speed * dy[direction]) % N
        world[new_x][new_y].append([mass,speed,direction])

    # 한 공간에 파이어볼이 2개 이상인지 확인
    for i in range(N):
        for j in range(N):
            # 2개 이상인 경우 4개의 파이어볼로 쪼갠다.
            if len(world[i][j]) > 1:
                total_mass, total_speed, odd_count, even_count, ball_count = 0, 0, 0, 0, len(world[i][j])
                while world[i][j]:
                    mass, speed, direction = world[i][j].pop()
                    total_mass += mass
                    total_speed += speed
                    if direction % 2: # 1,3,5,7 방향인 경우
                        odd_count += 1
                    else: # 0,2,4,6 방향
                        even_count += 1
                if odd_count == ball_count or even_count == ball_count:  # 모두 홀수이거나 모두 짝수인 경우
                    new_directions = [0, 2, 4, 6]
                else:
                    new_directions = [1, 3, 5, 7]
                if total_mass//5:  # 질량 0이면 소멸한다.
                    for direction in new_directions:
                        fireballs.append([i, j, total_mass//5, total_speed//ball_count, direction])

            # 파이어 볼이 1개인 경우
            if len(world[i][j]) == 1:
                fireballs.append([i, j] + world[i][j].pop())

print(sum([fireball[2] for fireball in fireballs]))