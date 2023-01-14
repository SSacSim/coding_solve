from collections import deque
stones = [3,2]
k = 1
# 짝수 시작
my_que = deque(stones[:k])
min_step = 999000000
now_max = max(stones[:k]) # 현재 max que 안 저장
min_step = now_max
for i in stones[k:]:

  my_que.append(i) 
  pop_number = my_que.popleft()

  if pop_number == now_max:
    now_max = max(my_que)
    if now_max < min_step:
      min_step = now_max

print(min_step if min_step < max(stones[-k:]) else max(stones[-k:]))
