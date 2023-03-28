from collections import deque
import sys
input = sys.stdin.readline
T = int(input().strip())
for t in range(T):

  p = input().strip()
  list_count = int(input().strip())
  temp = input().strip()
  temp = temp[1:-1] + ","
  temp_num_list = []
  temp_num = ""
  for i in temp:
    if i != ",":
      temp_num +=i
    else:
      if temp_num =="":
        break
      temp_num_list.append(int(temp_num))
      temp_num = ""
  num_list = temp_num_list
  my_q = deque(num_list)
  now_play = 1 # 1 > left 가 시작 , -1> right가 시작점

  flag = 0
  for i in p:
    if i == 'R':
      now_play *= -1
    else:
      if len(my_q) == 0:
        print("error")
        flag = 1
        break
      if now_play == 1:
        my_q.popleft()
      else:
        my_q.pop()

  if flag == 0:
    answer = "["
    for index, _ in enumerate(range(len(my_q))):
      if now_play == 1:
        answer += str(my_q.popleft())+','
      else:
        answer += str(my_q.pop())+','
    
    if answer[-1] == ",":
      answer = answer[:-1]
    print(answer + "]")

