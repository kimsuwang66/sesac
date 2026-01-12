def solution(numbers):
    n = len(numbers)

    numbers_set = set(numbers)
    full_set = set(range(1, n+2))

    remain_set = full_set - numbers_set
    
    return remain_set.pop()