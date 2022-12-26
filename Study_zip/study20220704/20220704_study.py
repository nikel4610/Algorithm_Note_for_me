import time

path = './testdata/test.txt'

fw = open(path, 'w', encoding='UTF-8')
# 'a' -> 텍스트 추가
fw.write('배고프다 \n')
fw.write('점심 머먹징 \n')
fw.write('write 성공! \n')
print(path, '파일저장 완료!')
fw.close()

time.sleep(2)
fr = open(path, 'r', encoding='UTF-8')
print(fr.read())
fr.close()
print()
