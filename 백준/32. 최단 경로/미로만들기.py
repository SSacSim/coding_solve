import heapq 
import sys
input = sys.stdin.readline
n = int(input().strip())

# matrix : 0 > 벽 , 1 공간 
matrix = []
memo = []
inf = 999999999

for _ in range(n):
    temp = list(map(int,input().strip()))
    matrix.append(temp)
    memo.append([ inf for i in range(n)])

heap_list = []

heapq.heappush(heap_list,[0,0,0 ]) # 벽 뚫은 수 , 현재 row, 현재 column

# 우 하 좌 상
dy = [0,1,0,-1]# row
dx = [1,0,-1,0]# column 
while heap_list:
    crash_brick , now_row, now_column = heapq.heappop(heap_list)

    # 이미 더 짧게 올 수 있는 경우 ( 이미 처리된 경우 ) 
    if crash_brick > memo[now_row][now_column] :
        continue
    
    # 4방향
    for i in range(4):
        next_row = now_row + dy[i]
        next_column = now_column + dx[i]
        
        # size안에 존재하는지 checking
        if next_row >= 0 and next_row < n and next_column >= 0 and next_column < n:
            # update 
            if memo[next_row][next_column] > crash_brick + abs(matrix[next_row][next_column] -1):
                memo[next_row][next_column] =  crash_brick + abs(matrix[next_row][next_column] -1)
                heapq.heappush(heap_list, [ memo[next_row][next_column] , next_row,next_column  ] )
print(memo[n-1][n-1])