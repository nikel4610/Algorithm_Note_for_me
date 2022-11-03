# DFS and BFS 참고
# https://cyc1am3n.github.io/2019/04/26/bfs_dfs_with_python.html

# https://school.programmers.co.kr/learn/courses/30/lessons/84512
# -> dfs이용해서 다시 풀어보기

# 근데 솔직히 잘 이해가 안감... 공부의 필요성을 느낀다!
# TODO 문제를 많이 풀어봐야 할거같음...

# DFS -> 재귀함수 또는 스택
# 하나 먼저 끝을 보고 그다음으로 넘어감
# DFS - 깊이 우선 탐색 -> 스택을 이용. 파이썬에서 리스트는 스택으로 구현되어 있음!
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]
# 방문노드
visited = [False] * len(graph)

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

    # 0번 노드가 없으니 1번 노드부터 탐색

dfs(graph, 1, visited)
# 1 2 7 6 8 3 4 5

# 예시: numbers를 조합하여 target을 만들 수 있는 경우의 수를 구하라
def solution(numbers, target):
    res = [0]
    def dfs(i, n, l):
        if i == len(l): # i가 l의 길이와 같아지면
            if n == target: # n이 target과 같으면
                res[0] += 1 # res[0]에 1을 더해준다
            return
        v = l[i] # v에 l의 i번째 값을 넣어준다
        dfs(i + 1, n + v, l) # dfs를 재귀적으로 호출한다
        dfs(i + 1, n - v, l)

    dfs(0, 0, numbers)
    return res[0]

numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers, target)) # 5

# ---------------------------------------------

# BFS -> 큐 (from collections import deque)
# 최단 경로 찾기
# 얕게 하나하나씩 살펴보고 넘어감(층층이 살펴본다)


# BFS - 너비 우선 탐색 - 큐(FIFO)를 이용. collections의 deque 이용!
from collections import deque

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * len(graph)


def bfs(graph, start, visited):
    # 시작 노드를 큐에다가 먼저 삽입(삽입할 때 파이썬 리스트[]로 감싸주기)
    queue = deque([start])
    # 시작 노드를 방문 처리
    visited[start] = True

    # 큐에서 노드를 pop하고 그 노드의 인접노드들을 탐색. 단, 큐가 빌(False)때 까지
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

bfs(graph, 1, visited)
# 1 2 3 8 7 4 5 6

# 예시: 게임 맵 최단거리 
from collections import deque

def solution(maps):
    h = len(maps)
    w = len(maps[0])
    maps[h-1][w-1] = -1
    # 상하좌우
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    visited = [[0]*w for _ in range(h)]
    q = deque()
    answer = 1
    q.append((0, 0, answer))

    # 큐가 빌때까지 반복함
    while q:
        x, y, answer = q.popleft()
        # 현위치에서 네가지 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 공간을 벗어나는 경우 무시
            if -1 < nx < h and -1 < ny < w:
                if maps[nx][ny] and visited[nx][ny] == 0:
                    maps[nx][ny] = answer + 1
                    visited[nx][ny] = 1
                    q.append((nx, ny, answer+1))

    return maps[h-1][w-1]

# ---------------------------------------------

# https://school.programmers.co.kr/learn/courses/30/lessons/81302
# 예시 문제 거리두기 확인하기 
import queue
D = ((-1, 0), (1, 0), (0, -1), (0, 1))

def bfs(place, row, col):
    visited = [[False for _ in range(5)] for _ in range(5)]
    visited[row][col] = True
    
    q = queue.Queue()
    q.put((row, col, 0))
    
    while not q.empty():
        curr = q.get()
        if curr[2] > 2:
            continue
        if curr[2] != 0 and place[curr[0]][curr[1]] == 'P':
            return False
        
        for i in range(4):
            nr = curr[0] + D[i][0]
            nc = curr[1] + D[i][1]
            if nr < 0 or nr > 4 or nc < 0 or nc > 4:
                continue
            if visited[nr][nc]:
                continue
            if place[nr][nc] == 'X':
                continue
            visited[nr][nc] = True
            q.put((nr, nc, curr[2] + 1))
    return True
    
def check(place):
    for r in range(5):
        for c in range(5):
            if place[r][c] == 'P':
                if bfs(place, r, c) == False:
                    return False
    return True
    
def solution(places):
    answer = []
    
    for place in places:
        if check(place):
            answer.append(1)
        else:
            answer.append(0)
    return answer