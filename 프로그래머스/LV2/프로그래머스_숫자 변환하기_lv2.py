x = 10
y = 40
n = 55

from collections import deque
my_que = deque([]) #[숫자 , 횟수]

my_que.append([x,0])
visit_dict = dict()

while True:
  print('my_que', my_que)

  if len(my_que) == 0: # 정답이 없을때
    answer = -1
    break

  pop_list = my_que.popleft()

  if pop_list[0] == y:  # 정답을 만났을때
    answer = pop_list[1]
    break

  # 3개연산
  if (pop_list[0] + n ) <= y:
    if (pop_list[0] + n ) not in visit_dict:
      visit_dict[(pop_list[0] + n )] = 1
      my_que.append([pop_list[0] + n , pop_list[1] + 1])
  if (pop_list[0] * 2 ) <= y:
    if (pop_list[0] * 2  ) not in visit_dict:
      visit_dict[(pop_list[0] * 2  )] = 1
      my_que.append([pop_list[0] * 2 , pop_list[1] + 1])
  if (pop_list[0] * 3 ) <= y:
    if (pop_list[0] * 3 ) not in visit_dict:
      visit_dict[(pop_list[0] * 3  )] = 1
      my_que.append([pop_list[0] * 3 , pop_list[1] + 1]) 

print(answer)