from collections import deque

import sys
input = sys.stdin.readline

n, k = map(int, input().split())

# 1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 
lst = deque(range(1, n+1))
result = []
#  이제 순서대로 K번째 사람을 제거한다. 
# -> 앞에서 k-1번 뒤로 보낸다. 그리고 제거한다.

# 이 과정은 N명의 사람이 모두 제거될 때까지 계속된다. 
#  예를 들어 (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.
while lst: # lst에 값이 있으면 반복을 진행 / 없으면 멈추기.
    for _ in range(k-1):
        remove_person = lst.popleft()
        lst.append(remove_person)
    
    remove_person = lst.popleft()
    result.append(remove_person)
# <3, 6, 2, 7, 5, 1, 4>
# print(result)
print('<',", ".join(map(str, result)),'>', sep='')