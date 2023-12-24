import sys
sys.setrecursionlimit(100000)

#백트레킹, N-Queen 

N=int(sys.stdin.readline())

x=[0]*(N) #answer 이 들어 있는 배열
y=[0]*(N) #j값을 인덱스
diagorl=[0]*(2*(N)-1) #/ 대각선 i+j 값을 인덱스로
diagolr=[0]*(2*(N)-1) #\ 대각선 i-j+(N-1) 값을 인덱스로

position=list(map(int,sys.stdin.readline().split()))
correct=True

check=[] # 아직 배정되지 않는 i 값들의 인덱스
len_check=0

for i in range(N):
    if(position[i]!=0):
        x[i]=position[i]-1 #0~N-1 인덱스로 통일
        if(y[position[i]-1]==0 and diagorl[i+position[i]-1]==0 and diagolr[i-(position[i]-1)+N-1]==0):
            y[position[i]-1]=1
            diagorl[i+position[i]-1]=1
            diagolr[i-(position[i]-1)+N-1]=1
        else:
            correct=False
            break
    else:
        check.append(i)
        len_check+=1
        
def find(check_index):
    i=check[check_index]
    for j in range(N):
        if(y[j]==0 and diagorl[i+j]==0 and diagolr[i-j+N-1]==0):
            y[j]=1 
            diagorl[i+j]=1 
            diagolr[i-j+N-1]=1
            x[i]=j
            if(check_index+1<len_check): # 모든 칸을 다 채우지 못한 경우 다음 라인을 채우러 재귀 호출
                result=find(check_index+1)
            else: # 다 채우면 True를 반환
                return True
            if(result==True): 
                return True
            y[j]=0  # 원상 복구
            diagorl[i+j]=0 
            diagolr[i-j+N-1]=0
            x[i]=0
    
    return False
    
            
if( not correct or N==3):
    print(-1)
else:
    if(len_check):
        result=find(0)
        if(result==True): # 가능한 값이 있는 경우 그 값들을 출력
            for i in x:
                print(i+1,end=" ")
        else:
            print(-1) 
    else:
        for i in x:
            print(i+1,end=" ")
    
                
            