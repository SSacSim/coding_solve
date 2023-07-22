# 파일 합치기 
T = int(input())
K = int(input())

num_list = list(map(int,input().strip().split(" "))) 
matrix = [[num_list[row] if row == column else 999999999 for column in range(K)] for row in range(K)]
for plus in range(K):
    for row in range(K - plus):
        column = row + plus
        if row == column :
            continue
        else:
            for i in range(row ,column):
                value = 0
                print(row,column,i)
                if (row == i) & (column == (i+1)):
                    value = matrix[row][i] + matrix[i+1][column]
                else:
                    value += matrix[row][i] + matrix[i+1][column]
                    if (row != i) :
                        value += matrix[row][i]
                    if (column != i+1 ):
                        value += matrix[i+1][column]
                print(value)

                if matrix[row][column] > value :
                    matrix[row][column] = value
print(matrix[0][K-1])
