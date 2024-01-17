import sys
sys.setrecursionlimit(10000)
# 백트래킹
# N-Queen 문제와 비슷한 방식으로 접근하면 되나, 시간 복잡도를 신경 써야 한다.
# 비숍의 경우 흰색 칸에 있는 경우 흰색 칸만, 검은 칸에 있는 경우 검은 칸만으로 이동할 수 있는 특징이 있다.
# 따라서 홀수칸이랑 짝수칸은 서로 영향을 주지 못 하므로, 홀수칸끼리 1번, 짝수칸 끼리 1번 나눠서 계산해도 동일한 결과를 얻을 수 있다.
# 골드 1

N=int(sys.stdin.readline())
world=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]

diagonal=[0]*(2*N-1) # / 방향 (arr[i][j]에서 i+j의 합이 인덱스)
rev_diagonal=[0]*(2*N-1) # \ 방향 (arr[i][j]에서 (N-1)-i+j의 합이 인덱스)

#print(diagonal)
#print(rev_diagonal)

max_odd=0
max_even=0

# 백트래킹
def find_max_chess(i,count):
    global max_even, max_odd
    if(i%2==0):
        max_even=max(max_even,count)
    else:
        max_odd=max(max_odd,count)

    if( i>=2*N-1 ):
        return 0
    
    if(diagonal[i]==0):
        for j in range(i+1):
            if(0<=i-j<N and j<N and world[i-j][j]==1 and rev_diagonal[(N-1)-(i-j)+j]==0):     
                rev_diagonal[(N-1)-(i-j)+j]=1
                diagonal[i]=1
                find_max_chess(i+2,count+1)
                diagonal[i]=0
                rev_diagonal[(N-1)-(i-j)+j]=0
       
    find_max_chess(i+2,count)

find_max_chess(0,0) # 짝수 번째 칸만 탐색
find_max_chess(1,0) # 홀수 번째 칸만 탐색

print(max_odd+max_even)