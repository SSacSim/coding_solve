N = int(input())
matrix = [1 for i in range(10)] # 0 ~ 9 
for _ in range(N):
  for i in range(8 , -1 , -1):
    matrix[i] = (matrix[i + 1] + matrix[i]) %10007
print(matrix[0])