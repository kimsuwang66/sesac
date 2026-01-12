def solution(numbers, window):
    answer = []
    total = sum(numbers[:window])
    answer.append(total)

    for i in range(len(numbers) - window):

        total = total - numbers[i] + numbers[i+window]
        answer.append(total)
    return answer
solution([4,1,5,0,-4,1,-10], 3)