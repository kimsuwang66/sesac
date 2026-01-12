def solution(n):
    n = str(n)
    # 앞이랑 뒤랑 하나씩 비교한다.
    for left in range(len(n) // 2): # left는 왼쪽 절반 / right는 오른쪽 절반
        # print(left) # 0, 1, 2, 3, 4, 5, ... 이 되어야 해.
        # right라는 변수가 필요하고. # -1, -2, -3, -4, ...이 되어야 해.

        # left 랑 right랑 비교하는 것이 처음 <-> 끝을 비교하는 것이야.
        # left ---> 이동   right <---- 이동하면 전체를 비교할 수 있어.
        right = -1 - left # 음의 index

        if n[right] != n[left]:
            return False

    # for문을 다 비교해어 False가 한번도 안나왔어?
    return True
