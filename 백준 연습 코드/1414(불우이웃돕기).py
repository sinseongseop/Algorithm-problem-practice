import sys

# 문자열 처리, MST
#골드 3

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

def kruskal():
    global edges,computer_count, donation
    edges.sort()
    for edge in edges:
        cost,a,b=edge
        if(find(parent[a])!= find(parent[b])): 
            union(a,b)
            computer_count+=1
        else:
            donation+=cost



# main() 함수

N=int(sys.stdin.readline())
edges=[]

parent=[0]*N
for i in range(N):
    parent[i]=i

for i in range(N):
    link=sys.stdin.readline()
    for j in range(N):
        if(link[j]!='0'):
            if(0<=ord(link[j])-ord('a')<=25):
                cost=ord(link[j])-ord('a')+1
            else:
                cost=ord(link[j])-ord('A')+27

            edges.append([cost,i,j])


donation=0
computer_count=1
kruskal()
#print(edges) # 디버깅용

if(computer_count!=N):
    print(-1)
else:
    print(donation)