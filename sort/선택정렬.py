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
