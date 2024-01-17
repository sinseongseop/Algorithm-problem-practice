import sys
# 구현, 시뮬레이션
# 큐브의 각 면을 어떻게 배열로 저장할 건가? 큐브가 회전 할 때 각 면은 어떻게 변화되는 가? 
# 정육면체 전개도를 그려서 각 면마다 회전시 어떻게 변화는 지를 관찰하자.
# 시뮬레이션 장르는 때로는 노가다가 가장 빠른 길이다.
# 큐브의 각 면을 회전시킬때 인덱스 실수를 하기 쉬우니 주의해서 풀자. 
# 디버깅 연습하기 좋은 문제
# 삼성 SW 구현 연습 추천 문제
# 플래 5

cube=[]

# 큐브의 초기 상태를 설정하는 함수
def initialCube():
    global cube
    color=['w','r','y','o','g','b']
    
    cube=[[[0]*3 for _ in range(3)] for _ in range(6)]
    for part in range(6):
        for x in range(3):
            for y in range(3):
                cube[part][x][y]=color[part]

# part에 해당하는 index를 가진 큐브의 면의 색깔을 반시계방향으로 90도 회전시키는 함수
def rotate90CounterClockwise(part):
    global cube
    newCubePart=[[0]*3 for _ in range(3)]
    
    for i in range(3):
        for j in range(3):
            newCubePart[2-j][i]=cube[part][i][j]
    
    cube[part]=newCubePart

# part에 해당하는 index를 가진 큐브의 면을 시계방향으로 90도 회전시키는 함수
def roatate90Clockwise(part):
    global cube
    newCubePart=[[0]*3 for _ in range(3)]
    
    for i in range(3):
        for j in range(3):
            newCubePart[j][2-i]=cube[part][i][j]
    
    cube[part]=newCubePart
    
# 바라보는 면의 측면을 반시계방향으로 90도 회전시키는 함수 
def rotateSidePartCounterClockwise(part):
    global cube
    if(part==0):
        (cube[4][0][0],cube[4][0][1],cube[4][0][2],
         cube[1][0][0],cube[1][0][1],cube[1][0][2],
         cube[5][0][0],cube[5][0][1],cube[5][0][2],
         cube[3][0][0],cube[3][0][1],cube[3][0][2]
         )=(
        cube[3][0][0],cube[3][0][1],cube[3][0][2],
        cube[4][0][0],cube[4][0][1],cube[4][0][2],
        cube[1][0][0],cube[1][0][1],cube[1][0][2],
        cube[5][0][0],cube[5][0][1],cube[5][0][2])
        
    elif(part==1):
        (cube[0][2][0],cube[0][2][1],cube[0][2][2],
        cube[5][0][0],cube[5][1][0],cube[5][2][0],
        cube[2][0][2],cube[2][0][1],cube[2][0][0],
        cube[4][2][2],cube[4][1][2],cube[4][0][2]) =(
        
        cube[5][0][0],cube[5][1][0],cube[5][2][0],
        cube[2][0][2],cube[2][0][1],cube[2][0][0],
        cube[4][2][2],cube[4][1][2],cube[4][0][2],
        cube[0][2][0],cube[0][2][1],cube[0][2][2])

    elif(part==2):
        (cube[4][2][0],cube[4][2][1],cube[4][2][2],
         cube[1][2][0],cube[1][2][1],cube[1][2][2],
         cube[5][2][0],cube[5][2][1],cube[5][2][2],
         cube[3][2][0],cube[3][2][1],cube[3][2][2]
         )=(
        cube[1][2][0],cube[1][2][1],cube[1][2][2],
        cube[5][2][0],cube[5][2][1],cube[5][2][2],
        cube[3][2][0],cube[3][2][1],cube[3][2][2],
        cube[4][2][0],cube[4][2][1],cube[4][2][2])
    
    elif(part==3):
        (cube[0][0][2],cube[0][0][1],cube[0][0][0],
        cube[4][0][0],cube[4][1][0],cube[4][2][0],
        cube[2][2][0],cube[2][2][1],cube[2][2][2],
        cube[5][2][2],cube[5][1][2],cube[5][0][2]) =(
        
        cube[4][0][0],cube[4][1][0],cube[4][2][0],
        cube[2][2][0],cube[2][2][1],cube[2][2][2],
        cube[5][2][2],cube[5][1][2],cube[5][0][2],
        cube[0][0][2],cube[0][0][1],cube[0][0][0])
        
    elif(part==4):
        (cube[0][0][0],cube[0][1][0],cube[0][2][0],
        cube[1][0][0],cube[1][1][0],cube[1][2][0],
        cube[2][0][0],cube[2][1][0],cube[2][2][0],
        cube[3][2][2],cube[3][1][2],cube[3][0][2]) =(
    
        cube[1][0][0],cube[1][1][0],cube[1][2][0],
        cube[2][0][0],cube[2][1][0],cube[2][2][0],
        cube[3][2][2],cube[3][1][2],cube[3][0][2],
        cube[0][0][0],cube[0][1][0],cube[0][2][0])
        
    elif(part==5):
        (cube[0][2][2],cube[0][1][2],cube[0][0][2],
        cube[3][0][0],cube[3][1][0],cube[3][2][0],
        cube[2][2][2],cube[2][1][2],cube[2][0][2],
        cube[1][2][2],cube[1][1][2],cube[1][0][2])=  (
        
        cube[3][0][0],cube[3][1][0],cube[3][2][0],
        cube[2][2][2],cube[2][1][2],cube[2][0][2],
        cube[1][2][2],cube[1][1][2],cube[1][0][2],
        cube[0][2][2],cube[0][1][2],cube[0][0][2])

# 바라보는 면의 측면을 시계방향으로 회전시키는 함수 
def roatetSidePartClockwise(part):
    global cube
    if(part==0):
        (cube[4][0][0],cube[4][0][1],cube[4][0][2],
         cube[1][0][0],cube[1][0][1],cube[1][0][2],
         cube[5][0][0],cube[5][0][1],cube[5][0][2],
         cube[3][0][0],cube[3][0][1],cube[3][0][2]
         )=(
             
         cube[1][0][0],cube[1][0][1],cube[1][0][2],
         cube[5][0][0],cube[5][0][1],cube[5][0][2],
         cube[3][0][0],cube[3][0][1],cube[3][0][2],
         cube[4][0][0],cube[4][0][1],cube[4][0][2]
         )
    elif(part==1):
        (cube[0][2][0],cube[0][2][1],cube[0][2][2],
        cube[5][0][0],cube[5][1][0],cube[5][2][0],
        cube[2][0][2],cube[2][0][1],cube[2][0][0],
        cube[4][2][2],cube[4][1][2],cube[4][0][2]) =(
        
        cube[4][2][2],cube[4][1][2],cube[4][0][2],
        cube[0][2][0],cube[0][2][1],cube[0][2][2],
        cube[5][0][0],cube[5][1][0],cube[5][2][0],
        cube[2][0][2],cube[2][0][1],cube[2][0][0]
        )

    elif(part==2):
        (cube[4][2][0],cube[4][2][1],cube[4][2][2],
         cube[1][2][0],cube[1][2][1],cube[1][2][2],
         cube[5][2][0],cube[5][2][1],cube[5][2][2],
         cube[3][2][0],cube[3][2][1],cube[3][2][2]
         )=(
        cube[3][2][0],cube[3][2][1],cube[3][2][2],
        cube[4][2][0],cube[4][2][1],cube[4][2][2],
         cube[1][2][0],cube[1][2][1],cube[1][2][2],
         cube[5][2][0],cube[5][2][1],cube[5][2][2]
         )
    
    elif(part==3):
        (cube[0][0][2],cube[0][0][1],cube[0][0][0],
        cube[4][0][0],cube[4][1][0],cube[4][2][0],
        cube[2][2][0],cube[2][2][1],cube[2][2][2],
        cube[5][2][2],cube[5][1][2],cube[5][0][2]) =(
        
        cube[5][2][2],cube[5][1][2],cube[5][0][2],
        cube[0][0][2],cube[0][0][1],cube[0][0][0],
        cube[4][0][0],cube[4][1][0],cube[4][2][0],
        cube[2][2][0],cube[2][2][1],cube[2][2][2]
        )
        
    elif(part==4):
        (cube[0][0][0],cube[0][1][0],cube[0][2][0],
        cube[1][0][0],cube[1][1][0],cube[1][2][0],
        cube[2][0][0],cube[2][1][0],cube[2][2][0],
        cube[3][2][2],cube[3][1][2],cube[3][0][2]) =(
    
        cube[3][2][2],cube[3][1][2],cube[3][0][2],
        cube[0][0][0],cube[0][1][0],cube[0][2][0],
        cube[1][0][0],cube[1][1][0],cube[1][2][0],
        cube[2][0][0],cube[2][1][0],cube[2][2][0])
        
        
    elif(part==5):
        (cube[0][2][2],cube[0][1][2],cube[0][0][2],
        cube[3][0][0],cube[3][1][0],cube[3][2][0],
        cube[2][2][2],cube[2][1][2],cube[2][0][2],
        cube[1][2][2],cube[1][1][2],cube[1][0][2])=  (
        
        cube[1][2][2],cube[1][1][2],cube[1][0][2],
        cube[0][2][2],cube[0][1][2],cube[0][0][2],
        cube[3][0][0],cube[3][1][0],cube[3][2][0],
        cube[2][2][2],cube[2][1][2],cube[2][0][2])

# 큐브의 해당하는 part를 direction 방향으로 회전시키는 함수
def rotate(part,direction):
    cubeFaceValue={"U":0,"F":1,"D":2,"B":3,"L":4,"R":5} # 큐브의 위,앞,아,뒤,왼,오 순으로 0~5 번호를 매겨줌
    part=cubeFaceValue[part]
    if(direction=="+"):
        roatate90Clockwise(part)
        roatetSidePartClockwise(part)
    else:
        rotate90CounterClockwise(part)
        rotateSidePartCounterClockwise(part)

# main() 함수    
Test=int(sys.stdin.readline())

for _ in range(Test):
    N=int(sys.stdin.readline())
    instruction=list(sys.stdin.readline().rstrip().split())
    initialCube() # 큐브 초기화
    
    for i in range(N): # 명령어 수행
        rotate(instruction[i][0],instruction[i][1])
        #print(cube)
        #print()
        
    for i in range(3): # 큐브 윗면 출력
        for j in range(3):
            print(cube[0][i][j],end="")
        print()