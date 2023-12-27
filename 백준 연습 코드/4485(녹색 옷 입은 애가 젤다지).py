import sys
import heapq
#그래프 이론, 다익스트라, 최단 경로 
#골드 4

def dikstra(start,graph,distance): #다익 스트라 알고리즘
    heap=[]
    heapq.heappush(heap,(0,start))
    distance[start]=0
    while(heap):
        dist,now=heapq.heappop(heap)
        if(distance[now]<dist):
            continue
        for next,bt_cost in graph[now]:
            cost=dist+bt_cost
            if(distance[next]>cost):
                distance[next]=cost
                heapq.heappush(heap,(distance[next],next))


TestCount=0 #질의의 횟수
while(True):
    N=int(sys.stdin.readline())
    
    if(N==0): # 종료 조건
        break;
    
    TestCount+=1
    world=[]
    for _ in range(N):
        world.append(list(map(int,sys.stdin.readline().split())))
    
    INF=int(1e9)
    start=0

    graph=[[] for _ in range(N*N)]
    
    # 2차원 배열을 1차원 배열로 바꾼 후, 각 배열에 있는 값들은 방향 그래프 edge의 가중치로 여긴다.
    # ex) world[i][j]-> world[i+1][j] 인 경우  N*i+j -> N*(i+1)+j 의 방향 그래프이며, edge의 가중치로 world[i+1][j]의 값을 가짐
    for i in range(N): 
        for j in range(N):
            if(i-1>=0):
                graph[N*i+j].append((N*(i-1)+j,world[i-1][j]))
            if(i+1<N):
                graph[N*i+j].append((N*(i+1)+j,world[i+1][j]))
            if(j-1>=0):
                graph[N*i+j].append((N*i+j-1,world[i][j-1]))
            if(j+1<N):
                graph[N*i+j].append((N*i+j+1,world[i][j+1]))

    distance=[INF for i in range(N*N)]
    dikstra(start,graph,distance) # 0에서 각 노드까지의 최단거리 계산
    print("Problem %d: %d" %(TestCount,distance[N*N-1]+world[0][0])) # 최단거리에 초기 비용은 포함 안되어 있으므로 초기 비용 world[0][0]을 더해 준다.
