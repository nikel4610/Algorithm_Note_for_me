def solution(maps):
    answer = 0

    def bfs(x, y): # BFS 함수
        q = [(x, y)]
        while q:
            x, y = q.pop(0) # 큐에서 하나씩 꺼내기
            for i in range(4): # 상하좌우 탐색
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= m: # 맵을 벗어나면
                    continue # 무시
                if maps[nx][ny] == 1: # 벽이면
                    maps[nx][ny] = maps[x][y] + 1 # 거리를 더해줌
                    q.append((nx, ny)) # 큐에 추가
        return maps[n-1][m-1] # 도착지까지의 거리 반환

    n = len(maps) # 맵의 세로 길이
    m = len(maps[0]) # 맵의 가로 길이

    dx = [-1, 1, 0, 0] # 상하좌우
    dy = [0, 0, -1, 1] 

    answer = bfs(0, 0)

    if answer == 1:
        return -1
    
    return answer