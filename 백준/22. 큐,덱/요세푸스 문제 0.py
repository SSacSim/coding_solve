from collections import deque
N , K = map(int, input().split(" "))
my_q = deque([])
for i in range(1,  N + 1):
  my_q.append(i)

answer = []
while True:
  if len(my_q) == 0:
    break

  for j in range(K):
    pop_number = my_q.popleft()

    if j + 1 == K:
      answer.append(pop_number)
    else:
      my_q.append(pop_number)

answer_s = "<"
for i in answer:
  answer_s += str(i) +", "
answer_s =answer_s[:-2]+">"
print(answer_s)