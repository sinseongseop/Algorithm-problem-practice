import sys

# 투 포인터
# 골드 4


N = int(sys.stdin.readline().strip()) 
word = list(map(str, sys.stdin.readline().strip()))

start = 0 # 왼쪽 포인터
end = 0 # 오른쪽 포인터
currentLength = 1 # 현재 검사중인 부분 문자열의 길이
answer = 0 

check = set(word[0]) # 포인터 사이의 문자열에 포함된 알파벳들 
while start < len(word) -1 and end < len(word) -1:

    if len(check) > N :
        start += 1 
        currentLength -= 1
        answer = max(answer,currentLength) 
        check = set(word[start:end+1]) 
    else:
        end += 1 
        currentLength += 1 
        check.add(word[end]) 

if len(check) > N :
    answer = max(answer,currentLength-1)
else:
    answer = max(answer,currentLength) 

print(answer)
