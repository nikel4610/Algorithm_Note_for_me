def solution(k, dungeons):
    answer = 0
    dungeons.sort(key=lambda x: x[1], reverse=True)
    return answer