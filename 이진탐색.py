# 오름차순으로 정렬된 배열에서 원하는 숫자 찾는 알고리즘
# 1. 배열 전체의 중간값을 target과 비교
# 2. 중간값 > target 이면 왼쪽 부분만 선택
# 3. 왼쪽 부분의 중간값을 다시 target과 비교 -> 반복

target = 25
m_list = [30, 94, 27, 92, 21, 37, 25, 47, 25, 53, 98, 19, 32, 32, 7]
length = len(m_list)

m_list.sort()
left = 0 
right = length-1

while left<=right:
    mid = (left+right)//2 # 전체 배열의 중간값 선택
    if m_list[mid] == target:
        print(mid+1)
        break
    elif m_list[mid]>target:
        right = mid-1
    else :
        left = mid+1

# 예시 문제
# https://school.programmers.co.kr/learn/courses/30/lessons/64062

def solution(stones, k):
    answer = 0
    left = 1
    right = max(stones)

    while left <= right:
        mid = (left+right)//2
        cnt = 0
        for stone in stones:
            if stone < mid:
                cnt += 1
            else:
                cnt = 0
            if cnt == k:
                break
        if cnt == k:
            right = mid - 1
        else:
            left = mid + 1
            answer = mid
    return answer