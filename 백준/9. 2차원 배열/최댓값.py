matrix = []

for i in range(9):
    matrix.append(list(map(int,input().split(" "))))

print(matrix)

max_count = 0
max_i = 0
max_j = 0
for index_i, i in enumerate(matrix):
    for index_j,j in enumerate(i):
        if matrix[index_i][index_j] > max_count:
            max_count = matrix[index_i][index_j]
            max_i = index_i
            max_j = index_j
print(max_count)
print(max_i+1 ,max_j+1)
