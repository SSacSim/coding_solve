input_num = list(map(int,input().split(" ")))
chess = [1,1,2,2,2,8]
answer = []
for i, j in zip(chess,input_num):
  answer.append(i - j)
print(*answer)
