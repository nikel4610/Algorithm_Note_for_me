# phone_book[i]가 나머지 요소에 포함이 되어 있는지 검사
for i in range(len(phone_book)-1):
    # phone_book[i] == (나머지 요소)[확인하고자 하는 길이]
    if phone_book[i] == (phone_book[i+1])[:len(phone_book[i])]:
        answer = False
        break