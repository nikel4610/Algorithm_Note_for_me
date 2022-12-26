# 로그인 문제
def solution(id_pw, db):
    answer = ''
    for i in range(len(db)):
        if id_pw[0] == db[i][0]: # id_pw[0] -> 아이디 / db[i][0] -> db의 아이디
            if id_pw[1] == db[i][1]: # id_pw[1] -> 비밀번호 / db[i][1] -> db의 비밀번호
                answer = 'login'
                break
            else:
                answer = 'wrong pw'
                break
        else:
            answer = 'fail'
    return answer
# 리스트[i][j] -> i번째 리스트의 j번째 요소