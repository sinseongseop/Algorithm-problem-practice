import sys

N = int(sys.stdin.readline())

MOD = 1000000009

dp=[0]*100001
dp[0] = 1
dp[1] = 1
dp[2] = 2
dp[3] = 2
dp[4] = 3 
dp[5] = 3

for i in range(6,100001):
    dp[i] = (dp[i - 2] + dp[i - 4] + dp[i - 6]) % MOD

for i in range(N):
    num = int(sys.stdin.readline())
    print(dp[num] % MOD)
        