import sys
input = sys.stdin.readline
n, k = map(int,input().split(" "))

coin = []

for _ in range(n):
  coin.append(int(input()))

coin.sort()

matrix = [ 0 for _ in range(k+1) ]
matrix = [ 0 for _ in range(k+1) ]
for now_coin in coin:
  for index in range(1,k+1):
    if index == now_coin:
      matrix[index] += 1
    else:
      if index - now_coin >= 1:
        matrix[index] += matrix[index - now_coin]
print(matrix[k])
