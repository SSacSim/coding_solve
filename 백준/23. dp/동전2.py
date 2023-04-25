import sys
input = sys.stdin.readline

n , k = map(int,input().strip().split(" "))
num_list = []

for _ in range(n):
  input_num = int(input().strip())
  if input_num <= k :
    num_list.append(input_num)

inf = 999999999
matrix = [inf for _ in range(k + 1)] # 0 base
for i in num_list:
  matrix[i] = 1
for index in range(1,k+1): 
  for number in num_list:
    if index - number >= 0 and matrix[index - number] + 1 < matrix[index]:
      matrix[index] = matrix[index - number] + 1
if matrix[k] >= inf:
  print(-1)
else:
  print(matrix[k])
