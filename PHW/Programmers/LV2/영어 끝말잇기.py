def solution(n, words):
    answer = [0, 0]
    # 끝말잇기
    for i in range(1, len(words)):
        if words[i-1][-1] != words[i][0] or words[i] in words[:i]:
            answer[0] = i%n + 1
            answer[1] = i//n + 1
            break
    return answer