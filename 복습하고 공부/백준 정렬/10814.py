import sys
input = sys.stdin.readline # 기본

n = int(input())
list = []

for i in range(n):
    a, b = map(str, input().split())
    list.append([int(a), i, b])

list.sort()
for i in range(len(list)):
    print("%d %s"%(list[i][0], list[i][2]))
    # 외우기
