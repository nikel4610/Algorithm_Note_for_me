# HashMap
# Key-Value의 쌍을 관리하는 클래스
# hashdict를 만들어 시작하자

# 문제 예시
# 수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.
#
# 마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열
# completion이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

# => 원하는 것
# participant는 있고 completion은 없는 선수의 이름을 return
def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()

    hashDict = {} # hash dict 생성
    sumHash = 0 # Participant의 hash값을 더할 변수

    for i in participant:
        hashDict[hash(i)] = i # hashdict에 participant의 hash값과 이름을 넣는다
        sumHash += hash(i) # participant의 hash값을 더한다

    # completion의 hash값을 빼준다
    for i in completion:
        sumHash -= hash(i)

    # 남은 값이 완주하지 못한 선수의 hash값이다
    return hashDict[sumHash]

# https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=ouo7581&logNo=221543909505
# from collections import Counter, deque, defaultdict
# 내용 확인 및 공부하기
dic = defaultdict('리스트')
for key, value in '리스트':
    dic[v].append(k)
# -> 이렇게 하면 dic에 '리스트'의 value가 key가 되어 붕복되는 부분이 value로 저장됨