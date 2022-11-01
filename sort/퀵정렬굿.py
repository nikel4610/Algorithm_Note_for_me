import sys
input = sys.stdin.readline

# 퀵 정렬
array = [...]

def quick_sort(array, start, end):
    if start >= end: # 원소가 1개인 경우 break
        return
    pivot = start # 피벗 = 첫번째 원소
    left = start + 1
    right = end
    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때 까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때 까지 반복
        while right > start and array[right] > array[pivot]:
            right -= 1
        if left > right: # 엇갈린다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array)


### 더 파이썬스러움
import sys
input = sys.stdin.readline

array = [...]

def quick_sort(array):
    # 리스트가 하나 이하의 원소만 담고 있다면 종료
    if len(array) <= 1:
        return array
    pivot = array[0] # 첫번째 원소(피벗)
    tail = array[1:] # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행 후, 전체 리스트 반환   
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))

# 가장 많이 사용됨
# 기준 데이터를 선정하고 큰 데이터, 작은 데이터의 위치를 바꾸는 아이디어 에서 착안
# 기준 데이터 = pivot
# 시간 복잡도는 O(NlogN)을 보장 -> 데이터가 무작위로 있을 때 가장 빠름 (거의 정렬 되어 있다면 대신 삽입 정렬 사용)

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array):
    # 재귀함수 종단 조건
    if len(array) <= 1:
        return array

    pivot = array[0] # 기준: 가장 첫번째 원소를 지정하자
    tail = array[1:]

    # Pivot값 기준으로 왼쪽은 모두 Pivot보다 작은 값, 오른쪽은 큰 값들
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

res = quick_sort(array)
print(res)