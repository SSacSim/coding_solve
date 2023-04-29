import sys
input = sys.stdin.readline

N = int(input().strip())
num_list = list(map(int,input().strip().split(" ")))
chain_list = [[x] for x in num_list ]
# 기준점
for index in range(N):
  # 모든 이전 데이터 살피기
  for j in range(index + 1):
    # 기준점 값이 이전 데이터 보다 크면 즉, 순열이면 
    if num_list[index] > num_list[j]:
      if len(chain_list[index]) < (len(chain_list[j]) + 1): 
        temp = chain_list[j].copy()
        temp.append(num_list[index])
        chain_list[index] = temp

answer_len = 0
answer_list = []
for index, i in enumerate(chain_list):
  if len(i) > answer_len:
    answer_len = len(i)
    answer_list = i


print(answer_len)
print(*answer_list)