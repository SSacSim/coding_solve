import sys
input = sys.stdin.readline
N = int(input().strip())
num_list = []
for _ in range(N):
  num_list.append(int(input().strip()))
oasis_stack = []

count = 0
for i in num_list:
  while True:
    if len(oasis_stack) == 0: # 텅 비었을 경우
      oasis_stack.append([i,1])
      break

    # 들어온 값이 stack의 마지막 값보다 큰 경우
    if oasis_stack[-1][0] < i:
      count += oasis_stack[-1][1]
      oasis_stack.pop()
    # 같은 경우 
    elif oasis_stack[-1][0] == i:
      count += oasis_stack[-1][1]
      oasis_stack[-1][1] += 1
      if len(oasis_stack) >1 : # 본인만 있는게 아니면
        count += 1
      break
    # 이하인 경우
    else:
      oasis_stack.append([i,1])
      count += 1
      break

print(count)
