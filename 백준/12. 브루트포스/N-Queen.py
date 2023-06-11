# 해당 문제는 queen의 범위를 체크하는 것에 대한 아이디어가 있어야함.
# 1. 1차원 배열을 통해 행,렬을 표시할 수 있음.
# 2. 1차원 배열의 index는 row / value 는 column을 뜻할 수 있음
# 3. 같은 index에 값이 존재한다면, 이미 queen의 범위에 포함
# 4. 1차원 배열 value에 같은 값이 존재한다면, 같은 column에 존재하는 것.
# 5. 대각선을 찾는 기법이 가장 인상깊었음. index - now_row == value - now_value 면, 대각선으로 겹치는 것.
# 6. 추가로 N * N 만큼 이동하면서 하면 시간초과가 나옴.
# 7. N번의 비교를 통해 진행해야함. 왜냐면, 이미 row에 놓았기 때문에 같은 row는 판단할 필요가 없음
# 8. 즉, 다음 row의 column에서만 비교하면 되므로, N번만 비교가능

import sys
import copy 
input = sys.stdin.readline
N = int(input().strip())

matrix = [ -1 for _ in range(N)]

def recur(start_row : int , matrix  , Q ):
  # print("=============")
  # print("input_matrix",matrix)
  # print("Q",Q)
  if Q == N:
    return 1
  answer = 0
  for point_index in range(0 , N ):

    if matrix[start_row] == -1 and (point_index not in matrix): # 같은 row에 존재하지 않음 + column에 존재하지 않음 
      flag = 0 
      for index, value in enumerate(matrix):
        if value == -1:
          continue
        if (abs(index - start_row) == abs(value - point_index)):
          flag = 1
          break
      if flag == 0: 
        temp_matrix = [item for item in matrix]
        # 해당 자리 퀸 놓기
        temp_matrix[start_row] = point_index
        answer += recur(start_row + 1 , [item for item in temp_matrix] , Q + 1)
  # print(answer)
  return answer
print(recur(0 , matrix,0))
