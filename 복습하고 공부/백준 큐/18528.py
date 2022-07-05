import sys
from collections import deque

input = sys.stdin.readline # 기본

n = int(input())
q = deque([])

def push(x):
    q.append(x)

def pop():
    if not q:
        return -1
    return q.popleft()

def size():
    return len(q)

def empty():
    if not q:
        return 1
    return 0

def front():
    if not q:
        return -1
    return q[0]

def back():
    if not q:
        return -1
    return q[-1]

for i in range(n):
    s = input().split()
    if 'push' in s:
        push(s[1])
    elif 'front' in s:
        print(front())
    elif 'back' in s:
        print(back())
    elif 'empty' in s:
        print(empty())
    elif 'size' in s:
        print(size())
    else:
        print(pop())
    