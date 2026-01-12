def solution(numbers):


    count_dic = {}
    most_common_value_count = 0
    most_common_value = 0
    # 모든 값을 확인합니다.
    for num in numbers:
        # 개수를 셀꺼에요.
        count_dic[num] = count_dic.get(num, 0) + 1

        # 지금까지 개수를 센 것들 중에서

        # 지금 센 개수가 지금까지 센 개수와 같다면
        # 최빈값을 작은 값으로 교체
        if count_dic[num] == most_common_value_count:
            if most_common_value > num:
                most_common_value = num

        # 지금 센 개수가 지금까지 센 개수보다 많으면
        # 데이터를 갈아끼웁니다.
        if count_dic[num] > most_common_value_count:
            # 최빈값 개수
            most_common_value_count = count_dic[num]
            # 최빈값 값.
            most_common_value = num
    
    return most_common_value


print(solution([1, 1, 2, 2, 2, 3, 3,2, 3, 4, 1, 2, -1, -3, -5 ]))
