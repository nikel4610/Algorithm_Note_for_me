# 알람시계 2884
H, M = map(int, input().split())

if M < 45:
    if H == 0:
        H = 23
        M += 60
    else:
        H -= 1
        M += 60
print(H, M - 45)

# 오븐시계 2525

H, M = map(int, input().split())
C = int(input())

H += C // 60
M += C % 60

if M >= 60:
    H += 1
    M -= 60
if H >= 24:
    H -= 24

print(H, M)


