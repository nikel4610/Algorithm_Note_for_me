# 세 개의 자연수 A, B, C가 주어질 때 A × B × C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.
# 예를 들어 A = 150, B = 266, C = 427 이라면 A × B × C = 150 × 266 × 427 = 17037300 이 되고, 계산한 결과 17037300 에는 0이 3번, 1이 1번, 3이 2번, 7이 2번 쓰였다.

import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())

num = list(str(a*b*c)) # 숫자 결과를 str -> list로 받아서 하나하나 분리
ans = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # 0부터 9까지

for i in num:
    ans[int(i)] += 1 # ans에 해당되는 숫자 있으면 1씩 더하기

for t in ans: 
    print(t) # 결과 출력
