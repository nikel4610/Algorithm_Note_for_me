name = ''
score, total = 0, 0

while True:
    name = input('이름입력: ')
    score = int(input('점수입력 '))
    if score == str(score):
        continue
    break

total = score + 11
print(f'{name}학생의 최종 점수는 {total}입니다.')