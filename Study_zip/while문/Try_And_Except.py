import sys
input = sys.stdin.readline

while True:
    try:
        a, b = map(int, input().split())
        print(a + b)
    except: # 더이상 테스트 케이스가 입력되지 않으면 except로 넘어가서 break
        break
# 정해놓은 발생오류가 발생하면 메시지와 함께 except문 수행하려면
# except 발생오류 as 메시지 :
