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

n = int(input())

inf = []
num = []

for _ in range(n):
    a, b = map(int, input().split())
    inf.append((a, b))

for i in range(n): ## 고르고 다음 -> for 겹쳐쓰기
    count = 0
    for j in range(n):
        if inf[i][0] < inf[j][0] and inf[i][1] < inf[j][1]:
            count += 1
    num.append(count + 1)

for d in num:
    print(d, end=" ")
