import sys
#CCW 알고리즘
x1,y1=map(int,sys.stdin.readline().split())
x2,y2=map(int,sys.stdin.readline().split())
x3,y3=map(int,sys.stdin.readline().split())

def ccw(x1,y1,x2,y2,x3,y3):
    cost=x1*y2+x2*y3+x3*y1-x2*y1-x3*y2-x1*y3
    if(cost<0):
        return -1
    elif(cost>0):
        return 1
    else:
        return 0
    
print(ccw(x1,y1,x2,y2,x3,y3))