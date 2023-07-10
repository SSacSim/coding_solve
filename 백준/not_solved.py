# https://www.acmicpc.net/problem/2573

row, column = map(int,input().strip().split(" "))
matrix = []

for _ in range(row):
    temp = list(map(int,input().strip().split(" ")))
    matrix.append(temp)

 # copy
temp_matrix = [ [ x for x in k ] for k in matrix ]

dx = [1 , 0 , -1 , 0 ]
dy = [0, 1 , 0 , -1 ]

for now_row in range(row):
    for now_column in range(column):
        if matrix[now_row][now_column] != 0 :
            # 4방향 0 갯수 체크 후 빼줌
            count = 0
            for i in range(4):
                next_row = now_row + dx[i]
                next_column = now_column + dy[i]
                
                if matrix[next_row][next_column] == 0 :
                    count += 1 
                
                temp_matrix[now_row][now_column] = max(0 , matrix[now_row][now_column] - count)

# bfs를 이용하여 두개 이상의 지역이 생기는지 체크.

from collections import deque

myq = deque([])

flag = 0
and_flag = 0
count_location = 0 
visit = [[1 if x == 0 else 0 for x in k] for k in temp_matrix]
for now_row in range(row):
    for now_column in range(column):
        if visit[now_row][now_column] == 0:
            count_location += 1
            # 방문하지 않은 곳.
            if flag == 1 :
                and_flag = 1 
                break
            flag = 1

            myq.append([now_row,now_column])
            visit[now_row][now_column] = 1 
            while True:
                pop_row, pop_column = myq.popleft()

                for i in range(4):
                    next_row = pop_row + dx[i]
                    next_column = pop_column + dx[i]
                    if temp_matrix[next_row][next_column] !=0:
                        visit[next_row][next_column] = 1
                        myq.append([next_row, next_column])
        
        if and_flag:
            break
    if and_flag:
        break
