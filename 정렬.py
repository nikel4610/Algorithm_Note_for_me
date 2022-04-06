list = []

list.sort() # 그냥 정렬 순서대로
list.sort(reverse = True) # 거꾸로 정렬
list.sort(key = lambda x:x[n]) # x[n] 기준으로 정렬해줌
# (x[n], x[n+1])
# n -> 정수

import sys
input = sys.stdin.readline

n = int(input())
list = []
count = 1

for i in range(n):
    a, b = map(int, input().split())
    list.append((a, b))

list.sort(key = lambda x:(x[1], x[0]))

end = list[0][1]
for i in range(1, n):
    if list[i][0] >= end:
        count += 1
        end = list[i][1]

print(count)

# 백준 1931 회의실 배정
