import sys
#수학, 정수론, 소수 판정, 에라토스테네스의 체

N=int(sys.stdin.readline())

K=N//2
answerA=((N-2+N-2*K)*K)//2 # X,Y,Z가 모두 N 이하이며, 서로 다른 개수 (등차 수열 합 공식 이용)

prime_num_flag=[True]*(N+1) # 에라토스테네스의 체를 위한 초기 작업
prime_num_flag[0]=False
prime_num_flag[1]=False

# 에라토스테네스 알고리즘 적용

for i in range(4,N+1,2): # 속도를 위해 2의 배수 먼저 따로 제거
    prime_num_flag[i]=False

for i in range(3,N+1,2): # 홀수들 중에서 소수 찾기
    if(prime_num_flag[i]==True):
        j=2
        while(i*j<=N): # 소수의 배수는 모두 제거
            prime_num_flag[i*j]=False
            j+=1

#print(prime_num_flag)

divisor_flag=[False]*(N+1) # 약수 인가? (True면 약수, False면 약수 아님)
divisor=[] # N의 약수들 

for i in range(1,N//2+1): #약수 판별
    if(N%i==0):
        divisor_flag[i]=True
        divisor.append(i)

divisor_flag[N]=True
divisor.append(N)

answerB=0 # X,Y,Z 가 모두 N의 양의 약수인 개수
for i in divisor:
    for j in divisor:
        if(i<=j and divisor_flag[i+j]):
            answerB+=1         

answerC=0
for i in range(2,N-1): # 소수+소수= 소수 가 되는 상황 판별 (쌍둥이 소수들 찾기)
    if(prime_num_flag[i+2] and prime_num_flag[i]):
        answerC+=1 
        
print(answerA)
print(answerB)
print(answerC)