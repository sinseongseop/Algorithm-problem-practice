import sys

#단순 규칙성 발견

N=int(sys.stdin.readline())

start=1
A=-1; B=1; C=1

for _ in range(1,N):
    saveA=A-C
    saveB=B+C
    saveC=2*A-2*B+C
    A=saveA
    B=saveB
    C=saveC

print(A+B+C)