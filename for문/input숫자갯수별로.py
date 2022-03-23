a = []
for i in range(9):
  a.append(int(input()))
  
# a 을 range(n)개까지 인풋

# 몇번째인지 출력
print(a.index(max(a))+1) # a의 최댓값이 몇번째인지
