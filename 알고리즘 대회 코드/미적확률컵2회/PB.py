import sys

#완전 탐색
#gcd 알고리즘 이용

N,M,K=map(int,sys.stdin.readline().split())
find_num=(3*M/K+1)-3
max_value=-1
a,b,c=0,0,0

def gcd(a,b):
    if(b>a):
        (a,b)=(b,a)

    c=a%b
    if(c==0):
        return b
    
    return gcd(b,c)

num=[0]*(N+1)
for _ in range(M-1):
    first,second,third =(map(int,sys.stdin.readline().rstrip().split()))
    num[first]+=1
    num[second]+=1
    num[third]+=1
    
for i in range(1,N+1):
    for j in range(i+1,N+1):
        for k in range(j+1,N+1):
            Pos=1-(num[i]+num[j]+num[k]+3)/(3*M)
            #print(Pos)
            if((Pos**K)*(1-Pos)>max_value):
                a,b,c=i,j,k 
                max_value=(Pos**K)*(1-Pos)


gcd_num=gcd((num[a]+num[b]+num[c]+3)*((3*M-(num[a]+num[b]+num[c]+3))**K),(3*M)**(K+1))
print((num[a]+num[b]+num[c]+3)*((3*M-(num[a]+num[b]+num[c]+3))**K)//gcd_num,(3*M)**(K+1)//gcd_num)
print(a,b,c)
