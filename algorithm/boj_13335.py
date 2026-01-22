from collections import deque
n, w, L = map(int, input().split())

trucks = deque(map(int,input().split()))

# 다리 라는 정보를 가지고 있습니다.
# 길이 w짜리 더미 데이터를 만들 것. 0 : 트럭이 올라갈 수 있는 곳
# 맨처음에는 list로 만들었다가, 필요지니 deque로 변경.
bridge = deque([0] * w)
weight = 0
time = 0

# 트럭이 다 움직일때까지 계속 반복.
while trucks:
    time += 1
    # bridge 위의 트럭이 움직입니다.
    # 왼쪽 트럭이 성공적으로 이동
    exit_truck = bridge.popleft()
    weight -= exit_truck

    # 트럭에서 빼다가 bridge로 이동시킵니다.
        # 무게가 가능할때만 이동합니다.
    if weight + trucks[0] <= L:
        new_truck = trucks.popleft()
        bridge.append(new_truck)
        weight += new_truck
    else:
        bridge.append(0) # 공간 차지용 데이터

print(time + w)