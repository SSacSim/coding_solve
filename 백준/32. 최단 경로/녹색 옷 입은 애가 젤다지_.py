import sys
import heapq
input = sys.stdin.readline

count = 0
while True:
    count += 1
    N = int(input().strip())
    
    if N == 0 :
        break
    
    matrix = []
    memo = []

    inf = 99999999999

    for _ in range(N):
        matrix.append(list(map(int,input().strip().split(" "))))
        memo.append([inf for _ in range(N)])
    import heapq

    memo[0][0] = matrix[0][0]
    heap_list = []

    heapq.heappush(heap_list, [memo[0][0] , 0 , 0 ]) # value , row , column

    # 우 하 좌 상
    dx = [1, 0, -1, 0] # column
    dy = [0, 1, 0, -1] # row
    while heap_list:
        pop_ = heapq.heappop(heap_list)
        base_value = pop_[0]
        now_row = pop_[1]
        now_column = pop_[2]
        
        # 4방향 search
        for i in range(4):
            next_row = now_row + dy[i]
            next_column = now_column + dx[i]
            
            # 범위 체킹
            if next_column >= 0 and next_column < N and \
                next_row >= 0 and next_row < N:
                    #값 체킹
                    if memo[next_row][next_column] > base_value + matrix[next_row][next_column]:
                        memo[next_row][next_column] = base_value + matrix[next_row][next_column]
                        heapq.heappush(heap_list, [memo[next_row][next_column] , next_row,next_column])
    print(f"Problem {count}: {memo[N-1][N-1]}")