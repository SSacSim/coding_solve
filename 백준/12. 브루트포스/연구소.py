import sys
input = sys.stdin.readline

matrix_row_len , matrix_column_len = map(int,input().strip().split(" "))
matrix = []
for _ in range(matrix_row_len):
  matrix.append(list(map(int,input().strip().split(" "))))

contami_point = []# [row,colum]

for i in range(matrix_row_len):
  for j in range(matrix_column_len):
    if matrix[i][j] == 2:
      contami_point.append([i,j])
    

from collections import deque
# 동 남 서 북
dx = [1 , 0 , -1 , 0]
dy = [0 , 1 , 0 , -1]
def bfs(start_list:list ,matrix ):
    '''
        start_list는 오염(2)가 있는 (row,column)쌍의 list
    '''
    visit = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

    my_q = deque([ ])
    count = 0
    for i in start_list:
        my_q.append([i[0], i[1]]) # row, column 순
        
    while my_q:
        now_row, now_column  = my_q.popleft()
            
        visit[now_row][now_column] = 1
        for i in range(4):
            next_row = now_row + dy[i]
            next_column = now_column + dx[i]
            # bounding check
            if next_row >= 0 and next_row < len(matrix) and next_column >= 0 and next_column < len(matrix[0]):
                if visit[next_row][next_column] == 0:
                    if matrix[next_row][next_column] == 0:
                        visit[next_row][next_column] = 1
                        my_q.append([next_row,next_column])
    
    #find 0
    for now_row in range(matrix_row_len):
      for now_column in range(matrix_column_len):
        if (visit[now_row][now_column] == 0) and (matrix[now_row][now_column] == 0):
            count += 1
    return count , visit, matrix
  

import copy
global_count = 0
def recur(start, new_matrix , set_):
    if set_ == 3:
        # bfs를 이용하여 오염되지 않은 위치 찾기
        result_bfs  , temp_visit , temp_matrix= bfs(contami_point , new_matrix)
        global global_count
        if result_bfs > global_count:
            global_count = result_bfs
        return 0

    for i in range(start , matrix_row_len * matrix_column_len):

        now_row = i // matrix_column_len
        now_column = i % matrix_column_len
        if new_matrix[now_row][now_column] == 0 : # 텅빈 공간
            # 벽을 쌓는다.
            temp = copy.deepcopy(new_matrix)
            temp[now_row][now_column] = 1
            recur(i + 1  , copy.deepcopy(temp) , set_ + 1 )
            
    
    # 현재 위치에 쌓는다.    
    # 현재 위치에 안쌓는다.
recur(0,matrix,0)

print(global_count)
