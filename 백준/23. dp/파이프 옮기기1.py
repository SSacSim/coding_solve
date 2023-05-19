N = int(input())
matrix = []
for _ in range(N):
    matrix.append(list(map(int,input().split(" "))))
ga = [[0 for _ in range(N)] for _ in range(N)]
dae = [[0 for _ in range(N)] for _ in range(N)]
sae = [[0 for _ in range(N)] for _ in range(N)]
input_ga = 1
for i in range(1,N):
    if matrix[0][i] == 1:
        input_ga = 0
    ga[0][i] = input_ga
for row in range(1,N):
    for column  in range(1,N):
        if matrix[row][column] == 0 : # 다음 위치
            ga[row][column] = ga[row][column - 1] + dae[row][column-1]
            sae[row][column] = sae[row - 1][column] + dae[row - 1][column]
        if matrix[row][column] == 0 and matrix[row - 1][column] == 0 and matrix[row][column - 1] == 0:
            dae[row][column] = dae[row-1][column-1] + ga[row-1][column-1] + sae[row-1][column-1]
print(ga[N-1][N-1] + dae[N-1][N-1] + sae[N-1][N-1])