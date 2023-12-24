import sys

# 수학, 수열 규칙성 발견, 애드혹
# 4/ 6/ 8 8 /10 10 /12 12 12 /14 14 14 /16 16 16 16/ 18 18 18 18 /... 
# 1개 1개 / 2개 2개 / 3개 3개 /4개 4개 /5개 5개 .... 로 값이 변함 (군수열)
# 시그마(N=1~ K) 2N = k(K+1) 이므로 K(K+1)<=N인 가장 큰 K를 찾음.(이차방정식의 해를 찾고 그 근처 정수 K 값 이용)
# 가장 적합한 값을 찾고 출력
# 골드 5

Test=int(sys.stdin.readline())

for _ in range(Test):
    tile_count=int(sys.stdin.readline())
    K=int((-1+(1+4*tile_count)**(1/2))//2)
    if(tile_count<=K*K):
        print(4*K)
    elif(tile_count<=K*K+K):
        print(2+4*K)
    elif(tile_count<=K*K+2*K+1):
        print(4+4*K)
    else:
        print(6+4*K)
    