import sys

# MST

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

def kruskal(edges):
    edges.sort()
    total=0
    
    for edge in edges:
        cost,a,b=edge
        if(find(parent[a])!=find(parent[b])):
            total+=cost
            union(a,b)

    return total
    
N=int(sys.stdin.readline())

positions=[]
edges=[]

for _ in range(N):
    x,y=map(float,sys.stdin.readline().split())
    positions.append((x,y))

for i in range(N-1):
    for j in range(i+1,N):
        first_x,first_y=positions[i]
        second_x,second_y=positions[j]
        distance=((second_x-first_x)**2+(second_y-first_y)**2)**(0.5)
        edges.append((distance,i,j))

parent=[0]*(N)
for i in range(N):
    parent[i]=i

print(kruskal(edges))