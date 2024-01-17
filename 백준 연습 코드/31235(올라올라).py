import sys

#greedy
#골드 4

N=int(sys.stdin.readline())
An=list(map(int,sys.stdin.readline().split()))
max_num=An[0] # 지금까지 본 값 중 가장 큰 값
min_k=1 # 최소 k값
now_k=1 # 조건을 만족시키기 위해 지금 필요한 k 값

for i in range(1,N):
    if(max_num<=An[i]):
        max_num=An[i]
        now_k=1
    else: # 지금 까지의 최댓값보다 작은 경우
        now_k+=1
        if(min_k<=now_k):
            min_k=now_k

print(min_k)
        
