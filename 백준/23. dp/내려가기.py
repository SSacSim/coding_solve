import sys
input = sys.stdin.readline
N = int(input().strip())

dp_min = [0,0,0] # 최소 memo
dp_max = [0,0,0] # 최대 memo
for _ in range(N):
  now_matrix = list(map(int,input().strip().split(" ")))
  
  min_list = []
  min_list.append(min(dp_min[:2]) + now_matrix[0])
  min_list.append(min(dp_min) + now_matrix[1])
  min_list.append(min(dp_min[1:]) + now_matrix[2])

  dp_min = min_list

  max_list = []
  max_list.append(max(dp_max[:2]) + now_matrix[0])
  max_list.append(max(dp_max) + now_matrix[1])
  max_list.append(max(dp_max[1:]) + now_matrix[2] )

  dp_max = max_list
  
print(max(dp_max),min(dp_min))