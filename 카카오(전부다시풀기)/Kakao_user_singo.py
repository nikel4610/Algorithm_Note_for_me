# 카카오 유저 신고

def solution(id_list, report, k):
    answer = []
    
    # report 중복 제거
    report = list(set(report))

    # 유저와 유저가신고한 유저를 딕셔너리로 저장
    user = {}
    for i in id_list:
        user[i] = []
    for i in report:
        user[i.split()[0]].append(i.split()[1])
    
    # 유저별 신고당한 횟수를 딕셔너리로 저장
    user_report = {}
    for i in id_list:
        user_report[i] = 0
    for i in report:
        user_report[i.split()[1]] += 1
    
    # 신고당한 횟수가 k번 이상인 유저를 딕셔너리로 저장
    user_k = {}
    for i in id_list:
        user_k[i] = 0
    for i in user_report:
        if user_report[i] >= k:
            user_k[i] = 1
    
    # user_k에 있는 유저가 신고한 유저에게 메일을 보냈을 때, 메일을 받은 유저의 수를 answer에 저장
    for i in user:
        count = 0
        for j in user[i]:
            if user_k[j] == 1:
                count += 1
        answer.append(count)

    return answer