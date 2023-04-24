import sys
input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
  N = int(input())
  coin_list = list(map(int,input().strip().split(" ")))

  target = int(input().strip())

  memo = [ 0 for _ in range(target + 1)]
  memo[0] = 1
  for now_coin in coin_list:
    for i in range(now_coin , target+1):
      if memo[i - now_coin] != 0:
          memo[i] += memo[i-now_coin]
  print(memo[target])
