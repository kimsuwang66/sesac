# mat = []

# for _ in range(5):
#     mat.append(input())
mat = [input() for _ in range(5)]

# 최대 15이기 때문에
# 여기서 15보다 작은 word가 있을 수 있지만
# 그건 내부에서 처리함.
result = ""
for j in range(15):
    for i in range(5):
        # i번째 word에 대해
        # j번째 글자가 존재?
        if len(mat[i]) > j:
            result += mat[i][j]
print(result)
