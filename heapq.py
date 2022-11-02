import heapq
# 리스트 heap
heapq.heapify(list)
# 리스트 추가
heapq.heappush(list, item)
# 리스트 최소값 삭제 + 결괏값 리턴
result = heapq.heappop(list)

# deque
from collections import deque
# https://school.programmers.co.kr/learn/courses/30/lessons/118667

def solution(queue1, queue2):
    answer = 0
    target = (sum(queue1) + sum(queue2)) // 2
    
    dq1 = deque(queue1)
    dq2 = deque(queue2)
    
    dq1_sum = sum(dq1)
    
    while dq1_sum != target:
        if dq1_sum < target:
            num = dq2.popleft()
            dq1.append(num)
            dq1_sum += num
        
        elif dq1_sum > target:
            num = dq1.popleft()
            dq1_sum -= num
        
        if not dq2:
            return -1
        
        answer += 1
    return answer