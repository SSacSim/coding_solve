#행렬 곱셈 순서 
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
            left =  matrix[row][column - 1][1][0] * matrix[row][column - 1][1][1] * array_list[column ][1]
            right = array_list[row ][0] * array_list[row ][1] * matrix[row+1][column][1][1] 
            
            if (left+ matrix[row][column - 1][0]) <= (right+ matrix[row+1][column][0]):
                matrix[row][column] = [ left + matrix[row][column - 1][0],[matrix[row][column-1][1][0] , array_list[column][1]]]
            else:
                matrix[row][column] = [ right + matrix[row+1][column][0],[array_list[row ][0] , matrix[row+1][column][1][1]]]

print(matrix[0][N-1][0])
        
