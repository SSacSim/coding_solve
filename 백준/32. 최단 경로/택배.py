import heapq
import sys
input = sys.stdin.readline

n , m= list(map(int,input().strip().split(" ")))
inf = 99999999
memo = [[ inf for _ in range( n + 1)] for _ in range(n + 1)] # 1 base

for _ in range(m):
  temp_input = list(map(int,input().strip().split(" ")))
  memo[temp_input[0]][temp_input[1]] = temp_input[2]
  memo[temp_input[1]][temp_input[0]] = temp_input[2]

result = [[ "-" if i == j else 999999 for i in range(n)] for j in range(n)]

for k in range(1,n+1):
  heap_list = []

  s = k
  heapq.heappush(heap_list, [ 0 , s ]) # len , now_node
  dp = [ [inf , [s,]]  for _ in range(n+1)] # len, 움직인 위치
  dp[s][0] = 0

  while heap_list:
    now_len , now_node = heapq.heappop(heap_list)

    if now_len > dp[now_node][0]:
      continue

    for next_node, next_len in enumerate(memo[now_node]):
      if next_len == inf:
        continue
      
      if dp[next_node][0] > next_len + now_len:
        dp[next_node][0] = next_len + now_len
        temp_copy = dp[now_node][1].copy()
        temp_copy.append(next_node)
        dp[next_node][1] = temp_copy
        heapq.heappush(heap_list , [dp[next_node][0] , next_node ])
        
  for index, i in enumerate(dp[1:]):
    if index == s -1 :
      continue
    result[s - 1 ][index] = i[1][1]
    
for i in result:
  print(*i)
