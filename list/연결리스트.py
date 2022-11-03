# 노드를 이용한 연결리스트
# 연결 리스트: 삭제/삽입의 시간복잡도는 O(1)이지만, 탐색의 시간복잡도는 O(n)이다.
# 노드 정의
class ListNode:
    def __init__(self, val = 0, next=None):
        self.val = val
        self.next = next

# 연결 리스트 생성
head = ListNode(0)

# 노드 추가/삭제
curr_node = head

new_node = ListNode(1)
curr_node.next = new_node
curr_node = curr_node.next
# ... 반복

# 전체 연결리스트 출력 (탐색)
node = head
while node:
    print(node.val)
    node = node.next
    
# 노드 탐색 후 삭제
node = head
while node.next:
    if node.next.val == 2: # 2를 찾고 삭제
        next_node = node.next.next
        node.next = next_node
        break
    node = node.next

# -----------------------------------------------------------------
# https://namu.wiki/w/%EC%97%B0%EA%B2%B0%20%EB%A6%AC%EC%8A%A4%ED%8A%B8
# 노드 선언 -> 양방향 연결 리스트

# 예제 https://school.programmers.co.kr/learn/courses/30/lessons/81303
# 설명 참고 https://kimjingo.tistory.com/161
from collections import deque

class Node:
    def __init__(self):
        self.prev = -1 # 이전 노드 인덱스 저장
        self.next = -1 # 다음 노드 인덱스 저장
        self.is_delete = False # 삭제 여부

def solution(n, k, cmd):
    # 연결 리스트 초기화
    node_list = [Node() for _ in range(n)] # 노드 리스트 생성
    for i in range(n - 1):
        node_list[i].next = i + 1 # 1번 노드의 next는 i + 1
        node_list[i + 1].prev = i # i + 1번째 노드의 prev는 i
    
    # 삭제된 노드 처리
    del_stack = deque()

    cur = k # 현재 가리키고 있는 노드

    # 명령어 처리
    for c in cmd:
        if len(c) > 1:
            # 커맨드 입력 나누기
            c, move_size = c.split(' ')
            move_size = int(move_size)
        # 명령어를 확인하고 move_size만큼 이동
        if c == "U":
            for i in range(move_size):
                cur = node_list[cur].prev # 현재 노드의 이전 노드로 이동

        elif c == "D":
            for i in range(move_size):
                cur = node_list[cur].next # 현재 노드의 다음 노드로 이동

        elif c == "C":
            # 현재 노드 삭제
            node_list[cur].is_delete = True
            del_stack.append(cur) # 삭제한 노드를 del_stack에 저장

            # 삭제한 노드의 이전 노드와 다음 노드를 연결
            prev_node = node_list[cur].prev
            next_node = node_list[cur].next

            if prev_node != -1:
                node_list[prev_node].next = next_node # 이전 노드의 next를 다음 노드로 변경
            if next_node != -1:
                node_list[next_node].prev = prev_node # 다음 노드의 prev를 이전 노드로 변경
                cur = next_node # 현재 노드를 다음 노드로 변경
            else: # 삭제한 노드가 마지막 노드일 경우
                cur = prev_node # 현재 노드를 이전 노드로 변경

        elif c == "Z":
            del_node = del_stack.pop() # 삭제한 노드를 del_stack에서 꺼냄
            node_list[del_node].is_delete = False # 삭제한 노드의 is_delete를 False로 변경

            # 삭제한 노드의 이전 노드와 다음 노드를 연결
            prev_node = node_list[del_node].prev
            next_node = node_list[del_node].next

            if prev_node != -1: # 삭제한 노드가 첫번째 노드가 아닐 경우
                node_list[prev_node].next = del_node # 이전 노드의 next를 삭제한 노드로 변경
            if next_node != -1: # 삭제한 노드가 마지막 노드가 아닐 경우
                node_list[next_node].prev = del_node # 다음 노드의 prev를 삭제한 노드로 변경

    # 결과 생성
    answer = ''
    for node in node_list:
        if node.is_delete:
            answer += 'X'
        else:
            answer += 'O'
    return answer