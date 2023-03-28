import sys
input =sys.stdin.readline
T = int(input().strip())
sosu_matrix = [ 0 for _ in range(1000001)]
for i in range(2,1000001):
  for j in range(2,1000001):
    if i * j <= 1000000:
      sosu_matrix[i * j] = 1 # 소수가 아님
    else:
      break
sosu_matrix[0] , sosu_matrix[1] = 1, 1
for _ in range(T):
  target = int(input().strip())
  count = 0
  for i in range(2 , target // 2 + 1):
    
    if sosu_matrix[i] == 0 and sosu_matrix[target - i] == 0:
      count += 1
  print(count)
