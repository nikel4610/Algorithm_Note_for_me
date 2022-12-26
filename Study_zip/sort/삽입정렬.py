import sys
input = sys.stdin.readline

# 삽입 정렬(선택 정렬보다 효율적)
array = [...]

for i in range(1, len(array)):
    for j in range(i, 0, -1): # 인덱스 i 부터 1까지 1씩 감소하며 반복
        if array[j] < array[j-1]: # 인덱스 j의 값이 인덱스 j-1의 값보다 작다면
            array[j], array[j-1] = array[j-1], array[j] # 인덱스 j의 값과 인덱스 j-1의 값을 바꿔준다.
        else:
            break # 인덱스 j의 값이 인덱스 j-1의 값보다 크다면 반복을 멈춘다.

print(array)

# 시간 복잡도는 O(N^2)이다.
# 주어진 데이터가 거의 정렬이 되어 있다면 매우 효율적이다.
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)): # 0번째 데이터는 정렬된 것으로 가정
    for j in range(i, 0, -1): # i번째부터 1번째 idx까지 왼쪽으로 이동
        if array[j-1] > array[j]:
            array[j-1], array[j] = array[j], array[j-1]
        else:
            break
            
print(array)