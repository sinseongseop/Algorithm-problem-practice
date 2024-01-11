import sys

#수학, 소수 판정, 에라토스테네스의 체, 투 포인터
#골드 3

N=int(sys.stdin.readline())

# 에라토스테네스의 체 이용해 N 이하의 모든 소수 찾아 주기
prime=[]
prime_count=0
che=[True]*(N+1)
for i in range(2,int(N**(0.5))+1):
    if(che[i]==True):
        prime.append(i)
        prime_count+=1
        for j in range(2*i,N+1,i):
            che[j]=False

for i in range(int(N**(0.5))+1,N+1):
    if(che[i]==True):
        prime.append(i)
        prime_count+=1


# 투 포인터를 이용해 답 찾기
left_pointer=0
right_pointer=0
total=2
answer=0
#print(prime)

while(right_pointer<prime_count and left_pointer<=right_pointer):
    #print(total,left_pointer,right_pointer)
    if(total==N):
        answer+=1
        right_pointer+=1
        if(right_pointer<prime_count):
            total+=prime[right_pointer]
    elif(total<N):
        right_pointer+=1
        if(right_pointer<prime_count):
            total+=prime[right_pointer]
    else:
        total-=prime[left_pointer]
        left_pointer+=1

print(answer)