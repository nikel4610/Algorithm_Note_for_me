hap = 0
su = 0

for i in range(1, 11, 1):
    su += 1
    hap += i
    print(su, end = ' ')
    if su == 10:
        print(hap, end = ' ')
        break
        