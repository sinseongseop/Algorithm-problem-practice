import sys
#구현, 시뮬레이션
#골드 1

 # 정육면체 전개도는 총 11개가 존재
development_3mul4=[[[0,0,0,1],[1,1,1,1],[0,0,0,1]],[[0,1,0,0],[1,1,1,1],[0,0,0,1]],
             [[0,0,1,1],[1,1,1,0],[0,1,0,0]],[[0,0,1,0],[1,1,1,1],[0,0,1,0]],
             [[0,0,1,0],[1,1,1,1],[0,0,0,1]],[[0,0,1,0],[1,1,1,0],[0,0,1,1]],
             [[0,0,1,0],[1,1,1,1],[0,1,0,0]],[[0,0,0,1],[1,1,1,1],[1,0,0,0]],
             [[1,1,0,0],[0,1,1,0],[0,0,1,1]],[[1,1,0,0],[0,1,1,1],[0,0,0,1]],]

development_2mul5=[[[1,1,1,0,0],[0,0,1,1,1]]]

# 월드의 일부분이 전개도와 일치하는 것이 있는 지 확인한느 함수
def find_development():
    global answer
    for i in range(4):    
        for j in range(3):
            sub_world=[world[i][j:j+4],world[i+1][j:j+4],world[i+2][j:j+4]]
            if( sub_world in development_3mul4 ):
                #print(sub_world)
                answer=True

    if(answer==False):
        for i in range(5):
            for j in range(2):
                sub_world=[world[i][j:j+5],world[i+1][j:j+5]] 
                if( sub_world in development_2mul5):
                    #print(sub_world)
                    answer=True   
    
#월드를 90도 회전 시킨다.
def rotate_90():
    global world
    new_world=[[0]*6 for _ in range(6)]
    for i in range(6):
        for j in range(6):
            new_world[j][5-i]=world[i][j]

    world=new_world

#월드를 좌우 반전 시킨다.
def flip_matirx():
    global world
    for i in range(6):
        for j in range(3):
            world[i][j],world[i][5-j]=world[i][5-j],world[i][j]

# main()함수

for _ in range(3):
    answer=False
    world=[]
    for _ in range(6):
        world.append(list(map(int,sys.stdin.readline().split())))
    
    for _ in range(4):
        find_development() # 해당하는 전개도가 존재하는 지 확인
        rotate_90() # 월드를 90도씩 회전시킨다.
    
    flip_matirx() # 월드를 좌우로 뒤집는다.    
    
    for _ in range(4):
        find_development() # 해당하는 전개도가 존재하는 지 확인
        rotate_90() # 월드를 90도씩 회전시킨다.
    
    if(answer):
        print("yes")
    else:
        print("no")