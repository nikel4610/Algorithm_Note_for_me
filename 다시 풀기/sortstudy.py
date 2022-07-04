import sys
input = sys.stdin.readline # 기본

n = int(input())
list = []

for i in range(n):
    a, b = map(int, input().split())
    list.append([a, b]) # 2중 리스트
    # [[3, 4], [1, 1], [1, -1], ...] 이런식으로 출력됨

result = sorted(list)

for i in range(n):
    print(result[i][0], result[i][1])
    # i에 0부터 쭉쭉 돌아가며 인덱싱
