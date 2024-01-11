import sys
#MST
#골4

#union-find 알고리즘
def find(i):
    global parent
    if(parent[i]!=i):
        parent[i]=find(parent[i])
    return parent[i]

def union(a,b):
    global parent
    a=find(a)
    b=find(b)
    
    if(a<b):
        parent[b]=a
    else:
        parent[a]=b


# 크루스칼 알고리즘
def kruskal():
    global edges,parent,answer
    
    edges.sort()
    
    max_cost=0
    for edge in edges:
        cost,a,b=edge

        if(find(a)!=find(b)):
            answer+=cost
            max_cost=max(max_cost,cost)
            union(a,b)

    answer-=max_cost


#main() 함수
N,M=map(int,sys.stdin.readline().split())

edges=[]

for _ in range(M):
    a,b,cost=map(int,sys.stdin.readline().split())
    edges.append((cost,a,b))

answer=0

parent=[0]*(N+1)

for i in range(N+1):
    parent[i]=i
    
kruskal()

print(answer)