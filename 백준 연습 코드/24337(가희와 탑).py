import sys
# greedy, 해 구성하기, 규칙 찾기
# a=1 인 경우랑 a!=1 인 경우랑 구분하여 생각
# 골드 3

N,a,b=map(int,sys.stdin.readline().split())

not_see_count=N-(a+b-1) # 가희와 단비에 의해 보이지 않는 건물의 개수 

if(not_see_count>=0):

    if(a>1): # a가 1보다 큰 경우 1 부터 시작 ex) 1 1 1 2 3 4 3 2 1
        for i in range(N-(a+b-1)):
            print(1,end=" ")
    
    for i in range(1,a):
        print(i,end=" ")

    if(a>=b): # 높이가 제일 높은 건물 높이 결정
        print(a , end=" ") # ex) 1 2 3 1
    else:
        print(b, end=" ") # ex) 1 3 2 1

    if(a==1): # a가 1인 경우 제일 큰 건물을 맨 앞에 세움  ex) 3 1 1 1 2 1
        for i in range(N-(a+b-1)):
            print(1,end=" ")
    
    for i in range(b-1,0,-1):
        print(i, end=" ")

else: # 불가능한 상황
    print(-1)    
    