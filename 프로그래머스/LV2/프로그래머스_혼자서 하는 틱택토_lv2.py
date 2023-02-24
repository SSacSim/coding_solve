board = ["OOO", "XX.", "..."]
matrix = [list(i) for i in board]
# O,X의 갯수 / X의 갯수가 O보다 크면 잘못된 것
count_O = 0
count_X = 0
answer = 1
for i in range(3):
  for j in range(3):
    if matrix[i][j] == "O":
      count_O +=1
    elif matrix[i][j] == "X":
      count_X +=1

print(count_O)
print(count_X)
O_flag=0
X_flag=0
if (count_X > count_O) or (count_O > count_X + 1):
  print("1")
  answer = 0

else:
  find_3mok = [
      [[0,0],[0,1],[0,2]],
      [[1,0],[1,1],[1,2]],
      [[2,0],[2,1],[2,2]],
      [[0,0],[1,0],[2,0]],
      [[0,1],[1,1],[2,1]],
      [[0,2],[1,2],[2,2]],
      [[0,0],[1,1],[2,2]],
      [[0,2],[1,1],[2,0]]
  ]

  # 3목을 만들 수 있는경우 총 8가지 경우의 수만 존재함
  # 조건 1) O가 3목을 형성, O의 갯수가 X보다 딱 1개 많아야함
  for i in find_3mok:
    if matrix[i[0][0]][i[0][1]] == matrix[i[1][0]][i[1][1]] == matrix[i[2][0]][i[2][1]] == "O":
      print(" O 3목 찾았다!:" , i)
      O_flag = 1
      if (count_O >0) and ((count_O - 1) != count_X):
        print("2")
        answer = 0
    elif matrix[i[0][0]][i[0][1]] == matrix[i[1][0]][i[1][1]] == matrix[i[2][0]][i[2][1]] == "X":
      print(" X 3목 찾았다!:" , i)
      X_flag = 1
      if (count_O >0) and  (count_O != count_X):
        print("3")
        answer = 0
    
  if O_flag == 1 and X_flag == 1 :
    print("4")
    answer = 0

  # 조건 2 )X가 3목을 형성, 0의 갯수와 X의 갯수가 딱 맞아야함
print(answer)