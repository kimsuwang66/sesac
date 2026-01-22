from collections import deque

while True:
    data = input()

    if data == '.':
        break
    stack = deque()
    is_valid = True

    for s in data:
        if s == '(' or s == '[' or s == '{':
            stack.append(s)

        elif s == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                is_valid = False
                break

        elif s == ']':
            if stack and stack[-1] == '[': 
                stack.pop()
            else:
                is_valid = False
                break
        
        elif s == '}':
            if stack and stack[-1] == '{': 
                stack.pop()
            else:
                is_valid = False
                break
    if stack:
        is_valid = False
    
    if is_valid:
        print('yes')
    else:
        print('no')
