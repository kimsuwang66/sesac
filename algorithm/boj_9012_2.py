from collections import deque
T = int(input())

for _ in range(T):
    data = input()
    count = 0
    is_valid = True
    # 열리는 괄호라면 stack에 넣어줍니다.
    # 닫히는 괄호라면, stack에 있는 열리는 괄호와 쌍이 되기 때문에 열리는 괄호를 pop
        # 사실은 열리는 괄호 pop -> 불가능할수도 있음.
    for s in data:
        if s == '(':
            count += 1
        else:
            if count: # 열리는 괄호가 들어있으면
                count -= 1
            else:
                is_valid = False
                break
    # stack에 뭔가 들어있으면 False -> 열리고 아직 안닫혀서
    if count:
        is_valid = False
    
    if is_valid:
        print('YES')
    else:
        print('NO')
