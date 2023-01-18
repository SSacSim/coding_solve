begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
use_words = [ 0 for _ in range(len(words))]

#bfs

from collections import deque
my_que = deque()
my_que.append([1,begin])

collect_flag = 0
while True:
  print("myque",my_que)
  count , now_begin = my_que.popleft()
  print("pop",now_begin)
  for idx, i in enumerate(words):
    if use_words[idx] != 0:
      continue
    
    diff_count = 0
    flag  = 0
    for b_char , w_char in zip(list(now_begin),list(i)):
      if b_char != w_char:
        diff_count += 1
      
      if diff_count >= 2:
        flag = 1
        break

    if flag == 0:
      use_words[idx] = 1
      my_que.append([count+1, i])
      if i == target:
        collect_flag = 1
        break
  if collect_flag == 1:
    print(count)
    break
  if len(my_que) == 0:
    print(0)
    break

print("종료")