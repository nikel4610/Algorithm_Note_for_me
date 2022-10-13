# 최소공배수 (여기선 n과 6의 최소공배수)
def solution(n):
    answer = 0
    for i in range(max(n, 6), (n*6)+1):
        if i%n == 0 and i%6 == 0:
            return i//6

# 소인수분해
def solution(n):
    answer = []
    for i in range(2, n+1): # 소인수분해라서 2부터 시작
        while n%i == 0: # 더이상 나눠지지 않을 때 까지 반복
            answer.append(i)
            n = n//i # 나누기
    return answer

# for 2번 사용 -> 합성수 구하기
def solution(n):
    answer = 0
    for i in range(2, n+1):
        for j in range(2, i):
            if i%j == 0:
                answer += 1
                break
    return answer

# dict 적용
dict['적용할거']

# 2진수를 10진수로
int('2진수', 2)
# 10진수를 2진수로
bin('10진수')

# 문자열 계산
eval('문자열')
