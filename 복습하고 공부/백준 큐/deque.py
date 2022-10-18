import math
from collections import deque

def solution(progresses, speeds):
    answer = []
    dq = deque()
    count = 1

    for i in range(len(progresses)):
        a = math.ceil((100 - progresses[i]) / speeds[i])
        dq.append(a)
    print(dq)

    while dq:
        # 다음 비교할 요소 줍기
        if count > 1:
            count -= 1
            now = dq.popleft()
            continue

        now = dq.popleft() # dq에 있는 요소를 하나씩 줍기

        # 주워온 요소와 다음 요소를 비교
        for i in dq:
            if now >= i:
                count += 1
            else:
                # 뒤의 요소가 더 크면 여태 주운 요소들을 answer에 추가
                break
        answer.append(count)
    return answer


from collections import deque


def solution(s):
    answer = True
    count = 0
    dq = deque(s) # 입력값을 바로 deque에 넣기

    while dq:
        # dq의 첫번째 요소 줍기
        a = dq.popleft()
        if a == ')':
            count -= 1
        elif a == '(':
            count += 1
            
        # 처음에 ')'가 나오면 컷
        # () 가 나오면 0임 -> OK
        # dq를 전부 보거나 ')'가 더 많이 나오면 컷
        if count < 0:
            answer = False
            break
    # 전부 다 본 후 '('가 많이 나오면 컷
    if count > 0:
        answer = False
    return answer

