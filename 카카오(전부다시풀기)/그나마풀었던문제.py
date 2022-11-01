# TODO -> 카카오(전부다시풀기) 문제 다시 풀어보기
# https://school.programmers.co.kr/learn/courses/30/lessons/17681
def solution(n, arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        bina = bin(arr1[i]|arr2[i])[2:] # 2진수 합쳐서 나옴
        answer.append(("0" *(n - len(bina)) + bina).replace("1", "#").replace("0"," "))
    print(answer)
    print(("0" *(n - len(bina)) + bina)) # 이 부분 이해가 안됨
    return answer

#----------------------------------------

# https://school.programmers.co.kr/learn/courses/30/lessons/42889
def solution(N, stages):
    answer = []
    a = len(stages)

    for i in range(1, N + 1):
        if a != 0:
            count = stages.count(i)
            answer.append((count / a, i))
            a -= count
        else:
            answer.append((0, i))
    answer.sort(key=lambda x: (-x[0], x[1]))
    return [x[1] for x in answer]


def solution(N, stages):
    answer = []
    fails = []
    total = len(stages)

    users = [0 for i in range(N + 1)]
    for stage in stages:
        users[stage - 1] += 1

    for i in range(N):
        if users[i] == 0:
            fails.append([i + 1, 0])
        else:
            fails.append([i + 1, users[i] / total])
            total -= users[i]

    answer = sorted(fails, key=lambda x: (-x[1], x[0]))
    answer = [i[0] for i in answer]
    return answer

#----------------------------------------

# https://school.programmers.co.kr/learn/courses/30/lessons/17682
def solution(dartResult):
    answer = 0
    a = ''
    list = []

    for i in dartResult:
        if i.isnumeric():
            a += i
        elif i == 'S':
            a = int(a) ** 1
            list.append(a)
            a = ''
        elif i == 'D':
            a = int(a) ** 2
            list.append(a)
            a = ''
        elif i == 'T':
            a = int(a) ** 3
            list.append(a)
            a = ''
        elif i == '*':
            if len(list) > 1:
                list[-2] = list[-2] * 2
                list[-1] = list[-1] * 2
            else:
                list[-1] = list[-1] * 2
        elif i == '#':
            list[-1] = list[-1] * -1

    print(list)
    return sum(list)

import re

def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)')  # 요 부분 참고!
    dart = p.findall(dartResult)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer

#----------------------------------------

# https://school.programmers.co.kr/learn/courses/30/lessons/118666
def solution(survey, choices):
    arr = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}
    result = ""

    for i, j in zip(survey, choices):
        if j < 4:
            arr[i[0]] += (4 - j)
        elif j > 4:
            arr[i[1]] += (j - 4)

    arr2 = list(arr.items())

    for i in range(0, len(arr2), 2):
        if arr2[i + 1][1] > arr2[i][1]:
            result += arr2[i + 1][0]
        else:
            result += arr2[i][0]

    return result

#----------------------------------------

# https://school.programmers.co.kr/learn/courses/30/lessons/92335
def is_prime(num):
    if num == 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num%i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    num = ''
    while n>0:
        num += str(n%k)
        n = n//k
    num = num[::-1]
    num = num.split('0')
    num = [int(num) for num in num if num !='']

    for i in range(len(num)):
        if is_prime(num[i]):
            answer += 1
    return answer

#----------------------------------------

