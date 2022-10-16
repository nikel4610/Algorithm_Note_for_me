# 케릭터의 움직임에 따라 위치 판별
# 보드의 중심은 0,0 위치해있음
def solution(keyinput, board):
    answer = []
    x = 0
    y = 0 # 처음 위치
    # 움직임 커맨드를 dict로 저장
    move = {'up': [0, 1], 'down': [0, -1], 'left': [-1, 0], 'right': [1, 0]}
    for i in range(len(keyinput)):
        x += move[keyinput[i]][0] # x축 움직임
        y += move[keyinput[i]][1] # y축 움직임
        if abs(x) > board[0]//2: # x축이 보드의 절반을 넘어가면
            x -= move[keyinput[i]][0] # 움직임 취소
        if abs(y) > board[1]//2:
            y -= move[keyinput[i]][1]
    answer = [x, y]
    return answer