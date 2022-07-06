import sys
input = sys.stdin.readline # 기본

n, m = map(int, input().split())
n_list = set()
m_list = set()

for i in range(n):
    n_list.add(input())
for i in range(m):
    m_list.add(input())

result = sorted(list(n_list & m_list))
print(len(result))

for i in result:
    print(i)