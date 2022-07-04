import sys
input = sys.stdin.readline # 기본

n = int(input())
list = []

for i in range(n):
    a, b = map(int, input().split())
    list.append([a, b]) # 2중 리스트

result = sorted(list)

for i in range(n):
    print(result[i][0], result[i][1])
