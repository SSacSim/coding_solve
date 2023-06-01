import heapq
import sys
input = sys.stdin.readline

n, m , r = map(int,input().strip().split(" "))
item = list(map(int,input().strip().split(" ")))
matrix = {}

for _ in range(r):
  input_list = list(map(int,input().strip().split(" ")))

  if input_list[0] not in matrix:
    matrix[input_list[0]] = [[input_list[1], input_list[2]]]
  else:
    matrix[input_list[0]].append([input_list[1], input_list[2]])

  if input_list[1] not in matrix:
    matrix[input_list[1]] = [[input_list[0], input_list[2]]]
  else:
    matrix[input_list[1]].append([input_list[0], input_list[2]])

global_max = 0
    
for i in range(1, n + 1):
  s = i
  inf = 999999999999999
  memo = [ inf for _ in range(n + 1)]
  visit= [ 0 for _ in range(n + 1)]
  memo[s] = 0

  heap_list = []

  heapq.heappush(heap_list,[ 0 ,  s ]) # len , now_node
  while heap_list:
    pop_ = heapq.heappop(heap_list) # lenth , now_node
    now_len = pop_[0]
    now_node = pop_[1]
    
    if now_node in matrix:
        for next_node in matrix[now_node]: # [0] : next_node, [1] : next_node len
          if now_len + next_node[1]< memo[next_node[0]]:
            memo[next_node[0]] = now_len + next_node[1]
            heapq.heappush(heap_list, [ memo[next_node[0]] , next_node[0]])
  
  local_max = 0 
  for k1, k2 in zip(memo[1:] , item):
    if k1 <= m:
      local_max += k2
  
  if local_max > global_max:
    global_max = local_max
print(global_max)
