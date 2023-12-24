import sys
import math

#페르마의 소정리 이용 문제
# (k!(n-k)!)^(p-1)=1 (mod p)
# (k!(n-k)!)^(p-2)=1/(k!(n-k)!) (mod p)
#(n!/k!(n-k)!)%P == ((n!%P)*((k!(n-k)!)^(p-2)%P))%P

N,M=map(int,sys.stdin.readline().split())

dp=[0]*(M+1)

dp[0]=1
fac=[0]*(N+1)
fac[0]=1

for i in range(1,N+1):
    fac[i]=i*fac[i-1]%998244353

for i in range(1,M+1):
    den = pow(fac[N-i]*fac[i], 998244353-2,998244353)
    dp[i]=fac[N]*den%998244353


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