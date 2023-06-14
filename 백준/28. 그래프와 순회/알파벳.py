import sys
input = sys.stdin.readline
R , C = map(int,input().strip().split(" "))
matrix = []
for _ in range(R):
    matrix.append(list(input().strip()))

# 우 하 좌 상
dx = [1, 0 ,-1 ,0] # column
dy = [0, 1, 0 ,-1] # row 
memo = [[1 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
def dfs(row , column, use_alpha):
    num = memo[row][column]
    for i in range(4):
        next_row = row + dy[i]
        next_column = column + dx[i]
        
        # boundary check
        if next_row >= 0 and next_row < len(matrix) and next_column >=0 and next_column < len(matrix[0]):
            # alpha check
            if use_alpha[ ord(matrix[next_row][next_column]) - 65 ] == 0 : # 사용하지 않은 곳이라면 dfs
                use_alpha[ ord(matrix[next_row][next_column]) - 65 ] = 1
                return_num = dfs(next_row,next_column, use_alpha)
                use_alpha[ ord(matrix[next_row][next_column]) - 65 ] = 0

                if num < return_num + 1 :
                    num = return_num + 1 
               
    return num
use_alpha = [0 for _ in range(26)]
use_alpha[ ord(matrix[0][0]) - 65] = 1
print(dfs(0,0,use_alpha))