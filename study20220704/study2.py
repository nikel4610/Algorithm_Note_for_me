import re

total = 0

a = 'apple 60 kg'
b = 'blue 30 km'

a = int(re.sub(r'[^0-9]', '', a))
b = int(re.sub(r'[^0-9]', '', b))

# apple = re.findall('\d+', a) -> '\d+' 숫자만 여러개 찾음
# blue = re.findall('\d+', b)
# total = apple + blue -> 리스트형이 됨


total = a+b

print('총 합계: ', total)