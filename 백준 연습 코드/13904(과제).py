import sys
# greedy, 정렬
# 골드 3

N = int(sys.stdin.readline())
assignment = []

for _ in range(N):
    assignment.append(list(map(int,sys.stdin.readline().split())))

assignment.sort(key=lambda x: (-x[1], x[0])) # 이익 내림차순, 마감일 오름차순 으로 정렬

#print(assignment) # 디버깅 용

score=[0]*1001

for todo in assignment:
    deadline = todo[0]
    for i in range(deadline , 0, -1):
        if(score[i] == 0):
            score[i] = todo[1]
            break

print(sum(score))         