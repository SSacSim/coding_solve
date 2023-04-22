n, k = map(int,input().split(" "))
matrix = [1 for _ in range(n + 1)]
for _ in range(k-1):
  for i in range(1,n+1):
    matrix[i] = (matrix[i] + matrix[i-1]) % 1000000000
print(matrix[n])
