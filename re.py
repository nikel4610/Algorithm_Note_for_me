import re
# https://brownbears.tistory.com/506 참고
re.sub('패턴', '바꿀문자열', '문자열', '바꿀횟수')
# re.sub(r'[^\w\s\.\-\_]', '', id) # 특수문자 제거

** fstring 과 rstring 차이
# https://armin.tistory.com/entry/pythonstring-%EB%AC%B8%EC%9E%90%EC%97%B4-%EC%95%9E-f-r-%EC%9D%98-%EC%9D%98%EB%AF%B8-formatter-string%EA%B3%BC-raw-string
>>> a = 1
>>> b = 2
>>> fs = f"{a} is a, {b} is b"
>>> 1 is a, 2 is b # 숫자가 적용됨

>>> rs = r"{a} is a, {b} is b"
>>> {a} is a, {b} is b # 그대로 출력