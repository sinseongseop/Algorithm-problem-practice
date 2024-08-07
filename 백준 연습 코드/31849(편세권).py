import sys
from collections import deque

# 그래프 탐색, bfs
# 골드 5

dxdy = [(0, 1), (1, 0), (0, -1), (-1, 0)]

N, M, R, C = map(int, sys.stdin.readline().split())
houses = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]
convenienceStores = [list(map(int, sys.stdin.readline().split())) for _ in range(C)]

world = [[-1] * (M + 1) for _ in range(N + 1)]

def bfs():
    global world
    que = deque()
    for x, y in convenienceStores:
        que.append((x, y))
        world[x][y] = 0  # 편의점 위치의 거리는 0
    while que:
        x, y = que.popleft()
        for dx, dy in dxdy:
            nx, ny = x + dx, y + dy
            if 1 <= nx <= N and 1 <= ny <= M and (world[nx][ny] == -1 or world[nx][ny] > world[x][y] + 1):
                world[nx][ny] = world[x][y] + 1
                que.append((nx, ny))

bfs()

answer = float('inf')

for x, y, cost in houses:
    if world[x][y] != -1:  # 유효한 거리만 고려
        answer = min(answer, world[x][y] * cost)

print(answer)