import sys

T = int(input())  # Test case
for i in range(T):
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)

# import sys
# 처음에 input = sys.stdin.readline 처음에 하고 int(input()) 이런식으로 하기
# 한개의 정수를 입력받을 때
a = int(sys.stdin.readline())

# 정해진 개수의 정수를 한줄에 입력받을 때
a, b, c = map(int, sys.stdin.readline().split())

# 임의의 개수의 정수를 한줄에 입력받아 리스트에 저장
data = list(map(int,sys.stdin.readline().split()))

# 임의의 개수의 정수를 n줄 입력받아 2차원 리스트에 저장
data = []
n = int(sys.stdin.readline())
for i in range(n):
    data.append(list(map(int,sys.stdin.readline().split())))

# 문자열 n줄을 입력받아 리스트에 저장
n = int(sys.stdin.readline())
data = [sys.stdin.readline().strip() for i in range(n)]

