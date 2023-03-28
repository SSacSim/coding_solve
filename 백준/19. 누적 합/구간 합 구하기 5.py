import sys
input = sys.stdin.readline
n,m = map(int,input().split(" "))
matrix = [[0 for _ in range(n + 1)] ] # 1base
for i in range(n):
  num_list = [0] + list(map(int,input().split(" ")))
  temp = []
  sum = 0
  for i in num_list:
    sum += i
    temp.append(sum)
  matrix.append(temp)
for i in range(m):
  find_list = list(map(int,input().split(" ")))
  start_x , start_y, end_x, end_y = find_list[0] , find_list[1] ,find_list[2] ,find_list[3]
  
  total_sum = 0
  for row in range(start_x , end_x + 1):
    total_sum  += (matrix[row][end_y] - matrix[row][start_y - 1 ])
  print(total_sum)
