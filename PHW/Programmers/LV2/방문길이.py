def solution(dirs):
    move = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    x, y = 0, 0
    map = []
    
    for i in dirs:
        dx, dy = move[i]
        nx, ny = x + dx, y + dy
        if not (-5 <= nx <= 5 and -5 <= ny <= 5): # 맵 벗어나면 무시
            continue
        map.append((x, y, nx, ny)) # 움직일 거리를 저장
        map.append((nx, ny, x, y)) # 움직이고 난 후의 거리를 저장
        x, y = nx, ny # 현재 위치를 업데이트

    return len(set(map)) // 2