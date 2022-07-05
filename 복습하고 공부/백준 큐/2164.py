import sys
import collections 

input = sys.stdin.readline # 기본

n = int(input())
a = collections.deque([i for i in range(1, n+1)])

while len(a) > 1:
    a.popleft()
    a.rotate(-1)

print(a[0])