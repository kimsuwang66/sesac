


# mat = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16]
# ]


# for i in range(len(mat)):         
#     for j in range(len(mat[i])):
#         print(mat[j][i], end=' ')

# print()

import sys
input = sys.stdin.readline
lst=[]


for i in range(1,6):
    lst.append(list(input()))

for i in lst:
    print(i)
    for j in range(i[i]):
        print(j)