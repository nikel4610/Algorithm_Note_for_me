kor, eng = map(int, input().split())

sum_score = kor + eng
avg_score = sum_score // 2

if avg_score > 70:
    print('합격')
else:
    print('불합격')
