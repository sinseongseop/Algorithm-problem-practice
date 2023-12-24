import sys

#union-find

N=int(sys.stdin.readline())
M=int(sys.stdin.readline())

world=[]
for i in range(N):
    world.append(list(map(int,sys.stdin.readline().split())))

parent=[]
for i in range(0,N+1):
    parent.append(i)

def find_parent(i):
    if(parent[i]!=i):
        parent[i]=find_parent(parent[i])
    return parent[i]

def union(x,y):
    x=find_parent(x)
    y=find_parent(y)

    if(x<y):
        parent[y]=x
    else:
        parent[x]=y

for i in range(N):
    for j in range(N):
        if(world[i][j]==1):
            union(i+1,j+1)

visit=list(map(int,sys.stdin.readline().split()))
success_flag=True

#print(parent)

for i in range(0,M-1):
    if(find_parent(visit[i])!=find_parent(visit[i+1])):
        success_flag=False
        break

if(success_flag):
    print("YES")
else:
    print("NO")