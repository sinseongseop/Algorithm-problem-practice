import sys

# 이분탐색, 매개변수 탐색
# 골드 4

N, M, L = map(int, sys.stdin.readline().split())
store=list(map(int, sys.stdin.readline().split()))

store.append(0)
store.append(L)
store.sort()

def binary_search(start, end, maxCount):
    maxDistance = L
    while(start <= end):
        mid = (start + end)//2
        #print(mid) #디버깅용
        count = 0
        for i in range(len(store)-1):
            count += (store[i+1] - store[i] - 0.01) // mid # 0.01을 빼주는 이유는, 나누어떨어지는 경우 1이 더 커져서, 나누어떨어지는 경우 방지
        
        if count > maxCount:
            start = mid + 1
        else:
            end = mid - 1
            maxDistance = min(maxDistance, mid)

    return maxDistance

print (binary_search(1, L, M ))