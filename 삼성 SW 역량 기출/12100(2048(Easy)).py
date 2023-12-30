import sys
#구현, 백트래킹, 시뮬레이션, 브루트포스

N=int(sys.stdin.readline())
initial_point=[] #초기 상태
max_point=0 # 가장 큰 블록(답)

for _ in range(N):
    initial_point.append(list(map(int,sys.stdin.readline().split())))

#왼쪽으로 미는 경우, 오른쪽으로 미는 경우, 위로 미는 경우, 아래로 미는 경우 각각 함수 작성

def left_move(point): # 왼쪽으로 미는 경우
    new_point=[[0]*N for _ in range(N)] # 새로운 판을 우선 다 0으로 초기화
    for i in range(N): # 한줄 씩 검사
        find_point=[] # 0이 아닌 점수들 저장
        len_find_point=0 # 0이 아닌 정수의 개수
        for j in range(N):
            if(point[i][j]!=0):
                find_point.append(point[i][j])
                len_find_point+=1
        change_point=[] # 새로운 점수들  
        com_flag=False # 바로 직전 점수들 끼리의 조합 여부 (ex) 2 2 2 2 인 경우 4 4 가 되어야 하므로  )
        for j in range(len_find_point):
            if(not com_flag):
                if(j<len_find_point-1 and find_point[j]==find_point[j+1]): # 연 달아 오는 두 수가 같은 경우
                    change_point.append(find_point[j]*2) # 수 합치기
                    com_flag=True #조합 여부 True로 변경
                else:
                    change_point.append(find_point[j])
            else: #두 수가 합쳐졌으면 통과하고 플래그 초기화
                com_flag=False
        for index,num in enumerate(change_point): # 새로운 판 점수 업데이트
            new_point[i][index]=num
    
    return new_point # 새로운 점수 반환

# 오른쪽으로 미는 경우, 위로 미는 경우, 아래로 미는 경우 모두 왼쪽으로 미는 경우 알고리즘과 유사하게 작성

def right_move(point): # 오른쪽으로 미는 경우
    new_point=[[0]*N for _ in range(N)]
    for i in range(N):
        find_point=[]
        len_find_point=0
        for j in range(N):
            if(point[i][j]!=0):
                find_point.append(point[i][j])
                len_find_point+=1
        change_point=[]                
        com_flag=False
        for j in range(len_find_point-1,-1,-1):
            if(not com_flag):
                if(j>0 and find_point[j]==find_point[j-1]):
                    change_point.append(find_point[j]*2)
                    com_flag=True
                else:
                    change_point.append(find_point[j])
            else:
                com_flag=False
        for index,num in enumerate(change_point):
            new_point[i][N-1-index]=num
    
    return new_point

def up_move(point): # 위로 미는 경우
    new_point=[[0]*N for _ in range(N)]
    for i in range(N):
        find_point=[]
        len_find_point=0
        for j in range(N):
            if(point[j][i]!=0):
                find_point.append(point[j][i])
                len_find_point+=1
        change_point=[]                
        com_flag=False
        for j in range(len_find_point):
            if(not com_flag):
                if(j<len_find_point-1 and find_point[j]==find_point[j+1]):
                    change_point.append(find_point[j]*2)
                    com_flag=True
                else:
                    change_point.append(find_point[j])
            else:
                com_flag=False
        for index,num in enumerate(change_point):
            new_point[index][i]=num
    
    return new_point

def down_move(point): # 아래로 미는 경우
    new_point=[[0]*N for _ in range(N)]
    for i in range(N):
        find_point=[]
        len_find_point=0
        for j in range(N):
            if(point[j][i]!=0):
                find_point.append(point[j][i])
                len_find_point+=1
        change_point=[]                
        com_flag=False
        for j in range(len_find_point-1,-1,-1):
            if(not com_flag):
                if(j>0 and find_point[j]==find_point[j-1]):
                    change_point.append(find_point[j]*2)
                    com_flag=True
                else:
                    change_point.append(find_point[j])
            else:
                com_flag=False
        for index,num in enumerate(change_point):
            new_point[N-1-index][i]=num
    
    return new_point

def mix_puzzle(count,point): # 5번 반복해서 모든 경우로 밀어보기
    #print(point)
    global max_point
    for line in point: # 최대 블록 값 계산
        max_point=max(max_point,max(line))
    
    if(count>5):
        return
     
    direction=[left_move,right_move,up_move,down_move]
    
    for doing in direction:
        new_point=doing(point)
        mix_puzzle(count+1,new_point)


#main 함수
mix_puzzle(1,initial_point)
print(max_point)