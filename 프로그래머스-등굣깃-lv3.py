m = 4 # 열
n = 3 # 행 

puddles = [[2,2]] # [열 행] [m n]

matrix = [[[-1,-1] for _ in range( m +1)] for _ in range(n+1)] # 1 base

matrix_flag = []
for i in range(n+1):
  temp = []
  for j in range(m+1):
    if (i == 0 )or (j == 0):
      temp.append(1)
    else:
      temp.append(0)

  matrix_flag.append(temp)
  
for i in puddles:
  matrix_flag[i[1]][i[0]] = 1
  
for column in range(1, m + 1): 
  for row in range(1, n + 1): # [열 행]
    if column == 1 and row == 1:
      continue
    if (matrix_flag[row - 1][column] == 1) and (matrix_flag[row][column - 1] == 1):
      matrix_flag[row][column] = 1

matrix[1][1] = [0,1]
count = 1
for column in range(1, m + 1): 
  for row in range(1, n + 1): # [열 행]
    if matrix_flag[row][column] == 1:
      continue
    # 좌측만 갈 수 있을때 
    if (matrix_flag[row][column - 1] == 0) and (matrix_flag[row - 1][column] == 1) :
      matrix[row][column] = [matrix[row][column - 1][0] +1 , matrix[row][column - 1][1] % 1000000007] # [step , count]
    
    # 상측만 갈 수 있을때
    elif ( matrix_flag[row - 1 ][column] == 0 ) and ( matrix_flag[row][column - 1] == 1 ):
      matrix[row][column] = [matrix[row - 1][column][0] +1 , matrix[row - 1][column][1] % 1000000007 ] # [step , count]
    # 다 갈 수 없을때 
    elif ( matrix_flag[row-1][column] == 1 ) and ( matrix_flag[row][column - 1] == 1 ):
      continue

    # 다 갈수 있을때 
    else: 
      if matrix[row - 1][column][0] < matrix[row][column - 1][0]:
        step = matrix[row - 1][column][0] + 1
        count = matrix[row - 1][column][1]
      elif matrix[row - 1][column][0] > matrix[row][column - 1][0]:
        step = matrix[row][column - 1][0] + 1
        count = matrix[row][column - 1][1]
      else:
        step = matrix[row][column - 1][0] + 1
        count = matrix[row - 1][column][1] + matrix[row][column - 1][1] 

      matrix[row][column] = [step,count % 1000000007] 
      
if matrix[n][m][1] >= 0:
    answer = matrix[n][m][1] 
else:
    answer = 0

print(answer)
