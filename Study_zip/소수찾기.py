t = int(input())
n = map(int, input().split())
count = 0
for i in n:
    a = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                a += 1
        if a == 0:
            count += 1
print(count)

#########

M = int(input())
N = int(input())
list = []

for i in range(M, N+1):
    a = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                a += 1
                break
        if a == 0:
            list.append(i)

if len(list) > 0:
    print(sum(list))
    print(min(list))
else:
    print(-1)
