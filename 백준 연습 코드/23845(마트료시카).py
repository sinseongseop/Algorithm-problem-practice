import sys
import heapq

#greedy, 우선 순위 큐, 스위핑
# 수가 연속해서 나온 개수* 연달아 나오는 수 중 최댓값 들의 합이 최대가 되기 위해서는 최대한 많은 수가 연달아 오면서, 제일 큰 수가 나오는 쪽으로 연달아 수가 나오게 하면 된다.
# 골드 3


N=int(sys.stdin.readline())
size=sorted(list(map(int,sys.stdin.readline().split()))) # 스위핑을 위해 오름차순으로 수들을 정렬해 준다.

#print(size)

heap=[]
total=0

for i in range(N):
    #print(heap)
    #print(total)
    
    if(not heap): #heap이 비어있는 경우
        heapq.heappush(heap,(size[i],-1)) #파이썬의 heapq는 최소 힙이므로 크기가 동일할때(big) 개수가 큰것(count)이 우선적으로 나오게 하기 위해서 음수로 처리 준다.

    else: #heap에 원소가 있는 경우
        big,count=heapq.heappop(heap)
        flag=True
        while(flag):
            if(size[i]>big+1): # 남아 있는 인형의 크기가 이전까지 본 인형과 크기가 2이상 차이 나는 경우 수가 연속해서 나온 개수* 연달아 나오는 수 중 최댓값을 처리해준다.
                total+=(-count)*big
                if(heap): #힙에 원소가 남아 있는 경우
                    big,count=heapq.heappop(heap)
                else: # 힙에 더 이상 원소가 없는 경우
                    heapq.heappush(heap,(size[i],-1))
                    flag=False
            elif(size[i]==big+1): #size가 1 차이 나는 경우( 연달아 오는 경우 )
                heapq.heappush(heap,(size[i],count-1))
                flag=False
            else: # size가 같은 경우
                heapq.heappush(heap,(big,count))
                heapq.heappush(heap,(size[i],-1))
                flag=False

while(heap):
    big,count=heapq.heappop(heap)
    total+=big*(-count)

print(total)            