def solution(n):
    answer = 0
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    answer = a%1234567
    return answer

# 문자열만 뽑기
c = list(filter(str.isalpha, a))
c =''.join(c)

# https://school.programmers.co.kr/learn/courses/30/lessons/131701
# ??? 이거 왜 안풀림 (진짜 모름)
