import sys

#단순 적분 계산

x1,x2=map(int,sys.stdin.readline().split())
a,b,c,d,e=map(int,sys.stdin.readline().split())

total=0
total=a//3*(x2**3-x1**3)+(b-d)//2*(x2**2-x1**2)+(c-e)*(x2-x1)
print(total)