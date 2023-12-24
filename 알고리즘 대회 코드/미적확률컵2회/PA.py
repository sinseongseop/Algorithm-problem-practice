import sys
import math
N,A,B,C=map(int,sys.stdin.readline().split())
print(math.factorial(N)//(math.factorial(A)*math.factorial(B)*math.factorial(C)))
      