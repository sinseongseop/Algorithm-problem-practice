import sys
import heapq
#자료 구조, 우선순위 큐, 그리디, 정렬
#골드 2

INF=int(10e9)

N,K=map(int,sys.stdin.readline().split())

bag_and_gem=[] # 가방과 보석을 한 리스트에 다 담는다.

for _ in range(N):
    bag_and_gem.append(list(map(int,sys.stdin.readline().split())))

for _ in range(K):
    bag_and_gem.append([int(sys.stdin.readline()),INF]) # 보석과 가방이 동일한 무게 일시 가방이 후 순위로 나오게 하기 위해 INF로 설정

bag_and_gem.sort() # (무게, 가치) 순으로 오름차순 정렬
 
total=0 #답
priority_que=[]

# 무게가 작은 순서대로 탐색 하고, 보석과 가방이 같은 무게 일 시 가방이 제일 마지막에 나오므로, 
# 가방에 이전에 탐색한 모든 보석 중 1개를 담기 가능.

for i in bag_and_gem:
    if(i[1]!=INF): # 보석 인 경우
        heapq.heappush(priority_que,-i[1]) # 우선순위 큐에 보석의 가치 추가,  최소 힙이므로 보석의 가치가 큰 것이 먼저 나오게 하기 위해 음수 처리
    else: # 가방 인 경우
        if(priority_que): # 담을 수 있는 보석이 존재 할 때
            total+=(-heapq.heappop(priority_que)) # 가장 가치가 큰 보석 선택

print(total)