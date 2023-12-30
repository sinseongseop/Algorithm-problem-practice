import sys

# 깡 구현
# 삼성 SW 역량 테스트 기출 문제
# 기존 코드 업그레이드 version
# 골드3

N,L=map(int, sys.stdin.readline().split()) #  지도 크기, 경사로 크기
world=[]
for _ in range(N):
    world.append(list(map(int,sys.stdin.readline().split())))

Road_count=0 # 길의 총 개수 (답안)

def find_road(): 
    global Road_count
    for i in range(N): # 가로 라인을 검사하면서 길인지 확인
        same_count=1 # 같은 높이의 연달아 있는 칸의 개수
        isRoad=True # 길 인가?
        isDownward=False # 내리막을 설치할 필요가 있는가?
        for j in range(1,N):
            if(abs(world[i][j]-world[i][j-1])>1): # 높이가 2 이상 차이 날 시 불가능
                isRoad=False
                break
            elif(world[i][j]==world[i][j-1]): # 높이가 같은 경우 same_count 값 1 증가
                same_count+=1
            elif(world[i][j]-world[i][j-1]==1): # 다음칸이 1 높은 경우
                if(isDownward): # 내리막을 설치할 필요가 있다면
                    if(same_count>=2*L): # 내리막과 오르막 둘다 설치해야하므로 2L 이상 필요
                        same_count=1
                        isDownward=False
                    else:
                        isRoad=False
                        break  
                    
                else: # 오르막만 설치 필요
                    if(same_count>=L):
                        same_count=1
                    else:
                        isRoad=False
                        break
    
            elif(world[i][j]-world[i][j-1]==-1): # 높이가 1 낮다면
                if(isDownward and same_count<L): # 내리막을 설치 해야 하는 데 설치가 불가능 한 경우
                    isRoad=False
                    break
                
                same_count=1
                isDownward=True # 내리막 길 설치 필요 flag 업데이트
        
        if(isDownward and same_count<L): # 내리막을 설치 해야 하는 데 설치가 불가능 한 경우
            isRoad=False
        
        if(isRoad): # 길이면 추가
            #print(i)
            Road_count+=1

def swap(arr,size): # 행과 열 바꾸기 (전치 행렬)
    for i in range(size):
        for j in range(i+1,size):
            (arr[i][j],arr[j][i])=(arr[j][i],arr[i][j])
            
find_road()
swap(world,N) # 행과 열을 서로 바꿈 (전치 행렬)
find_road()

print(Road_count) # 답 출력
