# ================================ not solved ========================
import sys
import copy 
input = sys.stdin.readline
N = int(input().strip())

matrix = [[ 0 for _ in range( N)] for _ in range( N )]


def recur(start_point : int , matrix  , Q ):
  # print("=============")
  # print("input_matrix",matrix)
  # print("Q",Q)
  if Q == N:
    return 1
  answer = 0
  for point_index in range(start_point ,  N * N  ):
    now_row = point_index // N
    now_column = point_index % N
    
    if matrix[now_row][now_column] == 0 :
      temp_matrix = [item[:] for item in matrix]
      # 해당 자리 퀸 놓기
      temp_matrix[now_row][now_column] = 1 
      # 8 방향 
      # 상 + 하
      for i in range(0 , N):
        temp_matrix[i][now_column] = 1
      # 우 + 좌
      for i in range(0, N):
        temp_matrix[now_row][i] = 1

      #상 +우
      temp_min = min( now_row, N - now_column - 1)
      for i in range(0 , temp_min):
        temp_matrix[now_row - (i + 1)][now_column + (i + 1)] = 1
      
      #하 +우
      temp_min = min( N - now_row - 1 , N - now_column - 1)
      for i in range(0 , temp_min):
        temp_matrix[now_row + (i + 1)][now_column + (i + 1)] = 1
      
      #상 +좌
      temp_min = min( now_row, now_column)
      for i in range(0 , temp_min):
        temp_matrix[now_row - (i + 1)][now_column - (i + 1)] = 1
      
      #하 +좌
      temp_min = min( N - now_row - 1 , now_column)
      for i in range(0 , temp_min):
        temp_matrix[now_row + (i + 1)][now_column - (i + 1)] = 1
      # print("now_row,column",now_row,now_column)
      # print("temp_matrix",temp_matrix)

      answer += recur(point_index + 1 , [item[:] for item in temp_matrix] , Q + 1)
  # print(answer)
  return answer
print(recur(0 , matrix,0))
