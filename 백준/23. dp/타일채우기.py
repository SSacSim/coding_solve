n = int(input())
matrix = [ 0 for _ in range(31)]
matrix[2] = 3
matrix[4] = 11

for i in range(5, n+1):
  result = 0
  if i % 2 != 1 : # 짝수일때만 진행
    result = result + (matrix[i - 2] * matrix[2])
    for j in range(i - 4 , 1 , -2):
      result +=  matrix[j] * 2 
    matrix[i] = result + 2
print(matrix[n])