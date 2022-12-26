import sys
input = sys.stdin.readline

array = [...]

for i in range(len(array)):
    min_index = i # 가장 작은 원소
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] # 자리 바꿈
    
print(array)

# for i in range(n):
#     for j in range(i+1):
#         result += time[j]
# (()) 2중 리스트 반복

# 시간 복잡도는 O(N^2)이다.
# 선택 정렬은 N번 만큼 가장 작은 수를 찾아서 맨 앞으로 보내야 하므로 총 N번의 반복이 필요하다.
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_idx = i
    for j in range(i+1, len(array)):
        if array[j] < array[min_idx]:
            min_idx = j
    # 위치 스와핑하기
    array[i], array[min_idx] = array[min_idx], array[i]

print(array)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]