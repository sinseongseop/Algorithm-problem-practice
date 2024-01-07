import sys

# 크루스칼 알고리즘 이용(MST(최소신장트리)를 구하는 알고리즘)
# Prim 알고리즘 역시 MST를 구하는 데 이용 가능

def find_parent(i):
    global parent
    if(parent[i]!=i):
        parent[i]=find_parent(parent[i])
    return parent[i]

def union(x,y):
    global parent
    x=find_parent(x)
    y=find_parent(y)

    if(x<y):
        parent[y]=x
    else:
        parent[x]=y


def kruskal(edges):
    edges.sort()
    total=0
    
    for edge in edges:
        cost,a,b=edge
        if(find_parent(a)!=find_parent(b)): # a와 b를 연결시 사이클이 형성 되지 않으면
            total+=cost
            union(a,b)
    
    return total


V,E= map(int,sys.stdin.readline().split())

parent=[]
for i in range(0,V+1):
    parent.append(i)

edges=[]
for _ in range(E):
    a,b,cost=map(int,sys.stdin.readline().split())
    edges.append((cost,a,b))

print(kruskal(edges))