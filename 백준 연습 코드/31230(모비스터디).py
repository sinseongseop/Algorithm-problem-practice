import sys
import heapq
#다익스트라, 최단 경로
#골드 3

#다익스트라 알고리즘
def dikstra(start,graph,distance):
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

#main() 함수

INF=int(10e16)
N,M,A,B=map(int,sys.stdin.readline().split())

graph=[[] for _ in range(N+1)]

for _ in range(M):
    a,b,cost=map(int,sys.stdin.readline().split())
    graph[a].append((b,cost))
    graph[b].append((a,cost))

A_distance=[INF for i in range(N+1)]
B_distance=[INF for i in range(N+1)]
dikstra(A,graph,A_distance)
dikstra(B,graph,B_distance)

min_distance=A_distance[B]
city=[]
for i in range(1,N+1):
    if(min_distance == A_distance[i]+B_distance[i]): # A->i->B 의 거리가 최단 경로랑 같을 시 i는 최단 경로 위의 집
        city.append(i)

#print(A_distance)
#print(B_distance)
print(len(city))
print(*city)