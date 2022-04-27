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
