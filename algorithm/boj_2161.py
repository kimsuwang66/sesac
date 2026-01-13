from collections import deque

n = int(input())

# 1 ~ n까지의 숫자를 담은 list가 필요함.
# 단, 삽입 삭제가 빈번히 일어날 것 같아서 list -> deque

lst = deque(range(1, n+1))
discard_lst = deque()
while lst: # 원소가 존재하면 True / 없음 False
    # 우선, 제일 위에 있는 카드를 바닥에 버린다. 
    popped_el = lst.popleft()
    discard_lst.append(popped_el) # 나중에 출력을 위해

    # 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.
    if lst:
        popped_el = lst.popleft()
        lst.append(popped_el)
# print(lst)
print(*discard_lst)