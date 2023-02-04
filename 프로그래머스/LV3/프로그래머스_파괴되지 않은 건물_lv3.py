board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]

cal_board = [ [0 for _ in range(len(board[0]))] for _ in range(len(board))]

for i in skill:
    start_x = i[1]
    start_y = i[2]
    end_x = i[3]
    end_y = i[4]
    
    # 누적합 구간 구하기
    if i[0] == 1:
        flag = -1
    else:
        flag = 1
        
    cal_board[start_x][start_y] += i[5] * flag # start x ,start y
    
    if end_y+1 < len(board[0]):
        cal_board[start_x][end_y + 1] -= i[5] * flag# start x , start y+1
        
    if end_x+1 < len(board):
        cal_board[end_x + 1][start_y] -= i[5] * flag# start x , start y+1    
    
    if end_x+1 < len(board) and end_y+1 < len(board[0]): 
        cal_board[end_x+1][end_y+1] += i[5] * flag# end x ,end y
    
    print(cal_board)
    print("============================")
    
    
    #[[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]
# 좌우 / 위 아래 누적합
# 좌우
for i in range(len(board)):
    for j in range(1, len(board[0])):
        cal_board[i][j] += cal_board[i][j-1] 
        
# 위 아래 
for i in range(len(board[0])):
    for j in range(1, len(board)):
        cal_board[j][i] += cal_board[j-1][i] 

count = 0
for i in range(len(board)):
    for j in range(len(board[0])):
        board[i][j] += cal_board[i][j]
        if ( board[i][j] )>0:
            count += 1
print(count)