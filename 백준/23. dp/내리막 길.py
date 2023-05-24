import sys
input = sys.stdin.readline
# bfs로 시작점에서 갈 수 있는 모든 경로를 구함. > visit checkt를 통해 방문한 위치 다시 확인 x
# bfs로 표시된 곳 (1) 인 곳만 업데이트?

# 500 * 500 = 250,000 > 완탐시 괜찮음? 
 
M , N  = map(int,input().split(" "))
matrix = []
 
for _ in range(M):
    matrix.append(list(map(int,input().split(" "))))

dp = [[0 for _ in range(N)] for _ in range(M)]
visit = [[0 for _ in range(N)] for _ in range(M)]

# 우 하 좌 상
dx = [1, 0, -1, 0]  
dy = [0, 1, 0, -1]
def dfs(x,y):
    if x == N-1 and y == M - 1:
        visit[y][x] = 1
        return 1
    
    if visit[y][x] == 1:
        return dp[y][x]
                
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if new_x >= 0 and new_x <N and new_y >= 0 and new_y < M:
            if matrix[y][x] > matrix[new_y][new_x]:
                return_number = dfs(new_x,new_y)
                visit[new_y][new_x] = 1
                dp[y][x] += return_number
    return dp[y][x]
dfs(0,0)
print(dp[0][0])
                
            
        