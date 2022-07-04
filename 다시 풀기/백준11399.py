import sys
input = sys.stdin.readline # 기본

n = int(input())
time = list(map(int, input().split()))

time.sort() # 1 2 3 3 4
result = 0

for i in range(n):
    for j in range(i+1):
        result += time[j] # 선택정렬 다시 보기
        
print(result)