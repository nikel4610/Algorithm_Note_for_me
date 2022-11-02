import heapq
# heappush (heqp이라는 리스트에 item추가)
heappush(heap, item)
# 기존 리스트를 heap으로 변환
heapq.heapify(list)
# 리스트 추가
heapq.heappush(list, item)
# 리스트 최소값 삭제 + 결괏값 리턴
result = heapq.heappop(list)

# https://www.daleseo.com/python-heapq/ 참고
# 최솟값 얻기(삭제 X)
heap[0]

# 최대 힙 뽑아보기
nums = [숫자들~~]
for num in nums:
    heappush(heap, -num) # 숫자를 큰 순서대로 heap에 넣기

while heap:
    heappop(heap)[1] # index 1 뽑기

# n번째 최소값/최대값
from heapq import nsmallest, nlargest, heappush, heappop

nsmallest('몇번쨰', ['리스트'])[-1] # n번째 작은 값
nlargest('몇번쨰', ['리스트'])[-1] # n번째 큰 값

# heap 정렬 
def heap_sort(nums):
  heap = []
  for num in nums:
    heappush(heap, num)

  sorted_nums = []
  while heap:
    sorted_nums.append(heappop(heap))
  return sorted_nums

print(heap_sort([4, 1, 7, 3, 8, 5])) # [1, 3, 4, 5, 7, 8]

# ----------------------------------------

# deque (heapq 아님)
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