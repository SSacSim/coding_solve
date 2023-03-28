import sys
input = sys.stdin.readline
N,M = map(int,input().strip().split(" "))
A = []
for _ in range(N):
  A.append(list(map(int,input().strip().split(" "))))

M,K = map(int,input().strip().split(" "))
B = []
for _ in range(M):
  B.append(list(map(int,input().strip().split(" "))))

answer = []
for i in A:
  temp = []
  for j in range(K):
    total_sum = 0
    for m in range(len(i)):
      total_sum += i[m] * B[m][j]
    temp.append(total_sum)
  answer.append(temp)

for i in answer:
  print(*i)