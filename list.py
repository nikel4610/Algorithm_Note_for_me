# 정수가 담긴 리스트 num_list가 주어질 때, num_list의 원소 중 짝수와 홀수의 개수를 담은 배열을 return 하도록 solution 함수를 완성해보세요.

def solution(num_list):
    answer = [0, 0]
    for i in num_list:
        if i % 2 == 0:
            answer[0] += 1
        elif i % 2 == 1:
            answer[1] += 1
    return answer

# 숫자 판별 -> isdigit()

# 각 자리 숫자 합
def solution(n):
    result = 0
    for i in str(n):
        result += int(i) # int로 변환해서 넣기
    return result

# 문자열 정렬
def solution(my_string):
    return ''.join(sorted(my_string.lower())) # -> 이게 가장 나은거 같음

# 문자열 삽입 (append, join X)
def solution(my_string, n):
    answer = ''
    for i in my_string:
        answer += i*n
    return answer

# 숫자중에 k가 있으면 그 숫자의 자릿수 출력
def solution(num, k):
    num = str(num)
    if str(k) in num:
        return num.index(str(k)) + 1
    else:
        return -1

# join은 str밖에 안됨 / int값 join 시키는 방법
# "".join(map(str, array)) -> count('숫자')로 갯수 세기
# count도 str만 갯수 세는거 가능해서 꼭 '' 붙여야됨

# ** 숫자 갯수 세는거 -> 그냥 str붙여서 문자열로 만들고 count('숫자')로 갯수 세기 or 확인하기
# -> 이때 문자열 추가 할 떄 + 사용

# 순서 상관없이 정렬 -> set
# 순서 고려해서 정렬 -> dict.fromkeys()