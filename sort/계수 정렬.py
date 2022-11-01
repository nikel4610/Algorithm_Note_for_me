import sys
input = sys.stdin.readline

# 계수 정렬
array = [...]

# 모든 범위를 포함하는 리스트 선언(모든 값을 0으로 초기화)
count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1 # 각 데이터에 해당하는 인덱스 값 증가

for i in range(len(count)): # 리스트에 기록된 정렬 정보 확인
    for j in range(count[i]):
        print(i, end=' ') # 띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력

# 제한된 크기 범위의 정수 형태로 데이터가 주어진 경우 사용하면 가장 좋음
# 데이터가 백만을 넘지 않을 때, 중복된 데이터가 여러개 있을 경우
# 주어진 데이터의 모든 범위를 담을 수 있는 크기의 빈 리스트 지정해줘야함
# 시간 복잡도는 O(N+K)이다.

array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

# 데이터 범위만큼의 빈 리스트 정의 => array의 길이만큼이라는 뜻은 아님!!! 왜냐면 중복된 값이 있을 수 있기 때문!
count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')