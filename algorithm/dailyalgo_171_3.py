def solution(numbers):

    # -1000 ~ 1000까지의 숫자를 가지고 있습니다.
    # list의 index에 맞춰서 넣고 싶어요.
    # -1000 ~ 1000까지의 숫자에 1000을 임의로 더합니다.
    # 그래서 끼워맞출꺼에요.

    tmp_value = 1000 # 임의로 더할 숫자.

    count_list = [0] * (1000 + tmp_value + 1)
    most_common_value_count = 0
    most_common_value = 0
    # 모든 값을 확인합니다.
    for num in numbers:
        num = num + tmp_value
        # 개수를 셀꺼에요.
        count_list[num] += 1 # list에 0을 이미 넣어와서.

        # 지금까지 개수를 센 것들 중에서

        # 지금 센 개수가 지금까지 센 개수와 같다면
        # 최빈값을 작은 값으로 교체
        if count_list[num] == most_common_value_count:
            if most_common_value > num:
                most_common_value = num

        # 지금 센 개수가 지금까지 센 개수보다 많으면
        # 데이터를 갈아끼웁니다.
        if count_list[num] > most_common_value_count:
            # 최빈값 개수
            most_common_value_count = count_list[num]
            # 최빈값 값.
            most_common_value = num
    
    return most_common_value - tmp_value


print(solution([1, 1, 2, 2, 2, 3, 3,2, 3, 4, 1, 2, -1, -3, -5 ]))
