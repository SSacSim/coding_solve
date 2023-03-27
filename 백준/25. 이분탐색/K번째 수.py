import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
left = 1
right = N * N
answer = 0
while True:
  if left > right:
    break
  mid = (right + left) // 2

  temp = 0
  for i in range(1,N + 1):
    temp += min(mid // i, N)
    
  if temp >= K: # mid
    right = mid - 1 
    answer = mid
  else:
    left = mid + 1

print(answer)
