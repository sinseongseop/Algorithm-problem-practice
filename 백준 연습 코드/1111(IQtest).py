import sys
#수학, 구현, 브루트포스, 많은 조건 분기
# y=ax+b 를 만족하는 a, b 쌍 찾기

N=int(sys.stdin.readline()) 
num=list(map(int,sys.stdin.readline().split()))
answer="B" #초기값을 답이 존재 하지 않음("B")로 설정
if(N==1):
    answer="A" # 1개만 존재 할 경우 무수히 많은 답 가능
elif(N==2):
    if(num[0]==num[1]): # ex) 10 10 이면 다음 수는 무조건 10 밖에 불가능
        answer=num[0] 
    else: # 그외의 경우 무수히 많은 답 가능. ex) 10 20 30 / 10 20 40 등
        answer="A"
else:
    for a in range(-200,201,1): # 주어지는 수의 절댓값이 100 이하이므로 a값이 엄청 큰 수는 불가능함.
        b=num[1]-num[0]*a
        for i in range(1,N-1,1):
            if(num[i]*a+b!=num[i+1]): # 만족하지 않으면 다음 a,b값으로
                break
            if(i==N-2): # 수열이 모두 (An+1)=a*(An)+b를 만족시키는 경우
                if(answer=="B"): # 처음 답을 도출한 경우 도출한 답 업데이트
                    answer=num[N-1]*a+b
                elif(answer!=num[N-1]*a+b): # 도출한 답과 다른 수열 답이 존재하는 경우 A(답이 여러가지 존재)를 출력
                    answer="A"
print(answer)
    