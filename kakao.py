# [TODO] -> 밑에 이해 안되는 부분 다시 공부
def solution(n, arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        bina = bin(arr1[i]|arr2[i])[2:]
        answer.append(("0" *(n - len(bina)) + bina).replace("1", "#").replace("0"," "))
    print(answer)
    print(("0" *(n - len(bina)) + bina)) # 이 부분 이해가 안됨
    return answer

