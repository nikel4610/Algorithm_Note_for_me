import sys
input = sys.stdin.readline

N, X = map(int, input().split())
A = list(map(int, input().split()))

for i in range(N):
    if A[i] < X: # 리스트에서 i번까지 쭉쭉 뽑아서 비교
        print(A[i], end=" ") # 가로로 출력하려면 ,end=" " 붙이기

def solution(numbers, direction):
    answer = []
    if direction == 'right':
        return numbers[-1:] + numbers[:-1]
    elif direction == 'left':
        return numbers[1:] + numbers[:1]
# 리스트 숫자 이동시키기 너무 어렵게 생각 ㄴㄴ
# 리스트에 뽑아서 다시 리스트에 넣는게 아니라 그냥 처음부터 리스트를 떄서 붙인다고 생각