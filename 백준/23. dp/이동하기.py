import sys
input = sys.stdin.readline
N , M = map(int,input().strip().split(" "))
matrix = []
for _ in range(N):
    matrix.append(list(map(int,input().strip().split(" "))))
memo_matrix = [[ 0 for _ in range(M)] for _ in range(N)]
memo_matrix[0][0] = matrix[0][0]
dx = [1,1,0] # 가로
dy = [0,1,1] # 세로
for i in range(N): # 세로 
    for j in range(M): # 가로
        for k in range(3):
            if ((i + dy[k]) < N) and ((j +dx[k]) < M):
                if memo_matrix[i +dy[k]][j + dx[k]] <  (memo_matrix[i][j] + matrix[i +dy[k]][j + dx[k]]):
                    memo_matrix[i +dy[k]][j + dx[k]] = memo_matrix[i][j] + matrix[i +dy[k]][j + dx[k]]     
print(memo_matrix[N-1][M-1])