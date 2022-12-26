def moveleft(s):
    return s[1:] + s[0]

def solution(s):
    answer = 0
    for i in range(len(s)):
        stack = []
        for j in s:
            if j in ['(', '[', '{']:
                stack.append(j)
            elif j == ')' and stack and stack[-1] == '(':
                stack.pop()
            elif j == ']' and stack and stack[-1] == '[':
                stack.pop()
            elif j == '}' and stack and stack[-1] == '{':
                stack.pop()
            else:
                stack.append(j)
        if not stack:
            answer += 1
        s = moveleft(s)
    return answer