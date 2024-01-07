import sys

# 선분 교차 판정, CCW

def ccw(x1,y1,x2,y2,x3,y3):
    if((x1*y2+x2*y3+x3*y1)-(x2*y1+x3*y2+x1*y3)>0):
        return 1
    elif((x1*y2+x2*y3+x3*y1)-(x2*y1+x3*y2+x1*y3)==0):
        return 0
    else: 
        return -1
    
x1,y1,x2,y2=map(int,sys.stdin.readline().split())
x3,y3,x4,y4=map(int,sys.stdin.readline().split())

#print(ccw(x1,y1,x2,y2,x3,y3)*ccw(x1,y1,x2,y2,x4,y4), ccw(x3,y3,x4,y4,x1,y1)*ccw(x3,y3,x4,y4,x2,y2))

if(ccw(x1,y1,x2,y2,x3,y3)*ccw(x1,y1,x2,y2,x4,y4)==0 and ccw(x3,y3,x4,y4,x1,y1)*ccw(x3,y3,x4,y4,x2,y2)==0):

    if(min(x1,x2)<=max(x3,x4) and max(x1,x2)>=min(x3,x4) and min(y1,y2) <= max(y3,y4) and max(y1,y2) >= min(y3,y4)):
        print(1)
    else:
        print(0)


elif(ccw(x1,y1,x2,y2,x3,y3)*ccw(x1,y1,x2,y2,x4,y4)<=0 and ccw(x3,y3,x4,y4,x1,y1)*ccw(x3,y3,x4,y4,x2,y2)<=0):
    print(1)
    
else:
    print(0)