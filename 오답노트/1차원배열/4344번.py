# 대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.
# **list로 받았으니 n은 list로 대우해야됨

import sys
input = sys.stdin.readline

a = int(input())

for i in range(a):
    n = list(map(int, input().split()))
    avg = sum(n[1:]) / n[0] # 정보를 뽑을때 리스트로 뽑기
    count = 0
    for j in n[1:]:
        if j > avg:
            count += 1
    result = count / n[0] * 100
    print("%.3f%%" % result)
   
# n[0] n[1] ~~
# 5 50 50 70 80 100 입력
# 40.000% 출력
