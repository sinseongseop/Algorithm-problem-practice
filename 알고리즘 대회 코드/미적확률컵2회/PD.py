import sys
import math

#그냥 조합 계산시 시간 초가 발생

N,M=map(int,sys.stdin.readline().split())

dp=[0]*(M+1)

dp[0]=1

for i in range(1,M+1):
    dp[i]=dp[i-1]*(N+1-i)//i 


twentysix=int(pow(26,N,998244353))
twentyfive=int(pow(25,N-M,998244353))

#print(twentyfive,twentysix)

total=0
save=twentyfive
for i in range(M):
    save=save*25%998244353
    total+=dp[M-1-i]*save%998244353
    total=total%998244353

#print(dp)
#print(total)

cal=(twentysix-total+998244353)%998244353
answer=((2*(dp[M]*twentyfive*cal)%998244353-(dp[M]*dp[M]*twentyfive*twentyfive)%998244353)+998244353)%998244353
print(int(answer))