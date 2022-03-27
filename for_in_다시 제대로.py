# 문자열 새로받아 숫자만큼 문자열 반복
a = int(input())
for i in range(a):
    b, c = input().split()
    for j in c:
        print(j*int(b), end='')
    print()
