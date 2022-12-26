import sys
input = sys.stdin.readline

a = int(input())
list = []

for i in range(a):
    list.append(int(input()))
result = sorted(list)
for i in range(len(list)):
    print(result[i])

