rows = 100
columns = 97
queries = [[1,1,100,97]]

matrix = []
matrix.append([0 for i in range(columns +1)]) # 1 base

# matrix 행렬 생성
for i_index , i in enumerate(range(rows)):
  temp = [0,]
  for j in range(1,columns + 1 ):
    temp.append(j + i_index * columns)
  matrix.append(temp)

def find_min(min_value, value):
  if min_value > value:
    return value
  else:
    return min_value

answer = []
for i in queries:
  start_row = i[0] # 2
  start_column = i[1] # 2 
  end_row = i[2] # 5
  end_column = i[3] # 4

  min_value = 2222222

  now_row = start_row
  now_column = start_column
  store_number = 0
  change_number = matrix[start_row][start_column]
  local_min_value = matrix[start_row][start_column]
  print(local_min_value)
  print("start_row",start_row)
  print("start_row",start_row)
  # 우
  for i in range(1, end_column - start_column + 1):
    temp_number = matrix[now_row][now_column + i]
    matrix[now_row][now_column + i] = change_number
    change_number = temp_number
    print("change_number" , change_number)
    local_min_value = find_min(local_min_value , change_number)
  now_column += (end_column - start_column)
  print(now_row)
  print(now_column)
  print("==============좌============================")
  
  # 하
  for i in range(1 ,end_row - start_row+ 1):
    temp_number = matrix[now_row + i][now_column ]
    matrix[now_row+i][now_column] = change_number
    change_number = temp_number
    local_min_value = find_min(local_min_value , change_number)
  now_row += (end_row - start_row)
  print(now_row)
  print(now_column)
  print("==============하============================")

  # 좌
  for i in range(1, end_column - start_column + 1):
    temp_number = matrix[now_row][now_column - i]
    matrix[now_row][now_column - i] = change_number
    change_number = temp_number
    local_min_value = find_min(local_min_value , change_number)
  now_column -= (end_column - start_column)
  print(now_row)
  print(now_column)
  print("==============우============================")

  # 상
  for i in range(1, end_row - start_row + 1):
    temp_number = matrix[now_row - i][now_column]
    matrix[now_row - i][now_column] = change_number
    change_number = temp_number
    local_min_value = find_min(local_min_value , change_number)
  now_row -= (end_row - start_row)
  print(now_row)
  print(now_column)
  print("==============상============================")
  # 한번만 진행되는 것을 보기위해
  answer.append(local_min_value)

print(answer)
