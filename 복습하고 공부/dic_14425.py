import sys
input = sys.stdin.readline # 기본

n, m = map(int, input().split())
arr = dict()
count = 0

for _ in range(n):
    s = input()
    arr[s] = True

for _ in range(m):
    t = input()
    if t in arr.keys():
        count += 1

print(count)