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

# ---------------------------------------------

