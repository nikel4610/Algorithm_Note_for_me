import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
result = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if a[i] + a[j] + a[k] > m:
                continue
            else:
                result = max(result, a[i]+ a[j]+ a[k])
print(result)
