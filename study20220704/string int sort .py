import sys
input = sys.stdin.readline # 기본

n = int(input())

list = []

for i in str(n):
    list.append(int(i))

list.sort(reverse=True)

for i in list:
    print(i, end='')