import sys
input = sys.stdin.readline 

N = int(input())
array_list = []

for _ in range(N):
    temp = list(map(int,input().strip().split(" ")))
    array_list.append(temp)
matrix = [[[0,array_list[row]]  if row == column  else [0,[]]for column in range(N)] for row in range(N)]
for plus in range(N):
    for row in range(N - plus): # 대각 으로 증가할 것임.
        if row == row +plus :
            continue
        else:
            column = row + plus 
            min_value = 999999999999
            min_location = 0
            for i in range(row , column):
                value = matrix[row][i][0] +  matrix[i+1][column][0] + matrix[row][i][1][0] * matrix[row][i][1][1] * matrix[i+1][column][1][1]

                if min_value >= value:
                    min_location = [matrix[row][i][1][0] , matrix[i+1][column][1][1]]
                    min_value = value
            matrix[row][column] = [min_value, min_location]

print((matrix[0][N-1][0]))
        
