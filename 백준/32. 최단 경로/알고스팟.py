import heapq
import sys
input = sys.stdin.readline

M, N = map(int,input().strip().split(" ")) # M : column, N : row
matrix = []
for _ in range(N):
    matrix.append(list(map(int,list(input().strip())))) # 0base
    
start_column, start_row = 0, 0
end_row,end_column = N - 1, M - 1  

# 다익보다는... 룰베이스?
inf = 99999999999999
memo = [[inf for _ in range(M)] for _ in range(N)]
memo[0][0] = 0

heap_list = []

# 우 하 좌 상
dx = [1 , 0 , -1 , 0]
dy = [0 , 1 , 0 , -1]
# heapq를 이용한 다익스트라
heapq.heappush(heap_list,[0 , start_row,start_column ]) # 뚫고간 벽 수 , row, column

while heap_list:
    pop_ = heapq.heappop(heap_list) # 뚫고간 벽 수 가장 낮은 
    now_row = pop_[1]
    now_column = pop_[2]
    
    # 4방향 체킹
    for i in range(4):
        # matrix를 벗어나는지 확인
        next_row = now_row + dy[i]
        next_column = now_column + dx[i]
        if next_row >= 0 and next_row < N and \
            next_column >= 0 and next_column < M:
                # 만약, 기록보다 작으면 
                if pop_[0] + matrix[next_row][next_column] < memo[next_row][next_column]:
                    memo[next_row][next_column] = pop_[0] + matrix[next_row][next_column]
                    # heap에 넣어주기
                    heapq.heappush(heap_list,[ memo[next_row][next_column],next_row,next_column])
print(memo[end_row][end_column])
    