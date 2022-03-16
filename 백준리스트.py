import sys
input = sys.stdin.readline

N, X = map(int, input().split())
A = list(map(int, input().split()))

for i in range(N):
    if A[i] < X: # 리스트에서 i번까지 쭉쭉 뽑아서 비교
        print(A[i], end=" ") # 가로로 출력하려면 ,end=" " 붙이기
