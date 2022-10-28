# deque 사용법
from collections import deque
# https://duckracoon.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-collections-deque-%EC%82%AC%EC%9A%A9%EB%B2%95%EA%B3%BC-%EC%9D%91%EC%9A%A9
q = deque('리스트')
deque.apppend() # 오른쪽에 추가
deque.appendleft() # 왼쪽에 추가
deque.clear() # 모든 요소 삭제
deque.insert('위치', '값') # 위치에 값 추가
deque.pop() # 오른쪽 요소 삭제 ** pop() 유용하게 많이 쓰이니까 기억하기
deque.popleft() # 왼쪽 요소 삭제
# TODO -> dq 문제 다시 풀기 + 링크 걸린 문제 다시 풀기
# https://school.programmers.co.kr/learn/courses/30/lessons/42885

# https://school.programmers.co.kr/learn/courses/30/lessons/42584
dq = deque('리스트')
while dq: # dq가 비어있지 않으면 반복

# 순열과 조합 참고
# https://velog.io/@dramatic/Python-permutation-combination-%EC%88%9C%EC%97%B4%EA%B3%BC-%EC%A1%B0%ED%95%A9
from collections import Counter
# 문자열 종류별로 갯수 카운터 해줌
Counter('문자열')

#합집합 교집합
sum(('리스트1' & '리스트2').values()) # 교집합
sum(('리스트1' | '리스트2').values()) # 합집합

# 특정 문자 찾기
# https://school.programmers.co.kr/learn/courses/30/lessons/49993
# 없으면 -1 return
~~.find('찾을 문자', '찾기 시작할 위치')
~~.startswith('시작하는 문자', '시작 지점') -> True or False 반환
~~.endswith('끝나는 문자', '시작지점', '끝나는 지점') -> True or False 반환
