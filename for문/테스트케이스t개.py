t = int(input()) # 테스트 케이스 개수 t개

# 입력받은 t만큼 반복
for _ in range(t):
  a, b = map(int,input().split())
  ~~

 # 1부터 n 까지의 합 출력
 n = int(input())
sum = 0
for i in range(1, n+1):
    sum += i
print(sum)

# 숫자 연속 입력을 따로따로 나누기
a = int(input())
b = int(input())
result = 0
for i in range(a):
    result += int(b[i]) # int(b[i] -> 숫자 따로 나누기
print(result)
