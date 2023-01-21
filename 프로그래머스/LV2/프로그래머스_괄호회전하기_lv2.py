s = "[](){}"
s_len = len(s)
from collections import deque

new_s = deque(list(s))
# 1,000,000 > 이여서 완탐 가능 
count = 0
for _ in range(s_len): # 1000
  
  left_temp = new_s.popleft() # 왼쪽 하나 뽑고
  
  new_s.append(left_temp)   # 오른쪽에 추가
  flag = 0
  
  temp_list = []
  print(new_s)
  for i in new_s: # 1000
    print("i",i)
    if i in ['}',')',']']:
      if len(temp_list) == 0:
        flag = 1
        break
      pop_char = temp_list.pop()

      if (pop_char == "{") and (i != "}"):
        flag= 1
        break
      elif (pop_char == "(") and (i != ")"):
        flag= 1
        break
      elif (pop_char == "[") and (i != "]"):
        flag= 1
        break
    else:
      temp_list.append(i)
    
  if len(temp_list) != 0:
    flag = 1

  if flag == 0:
    count += 1
  print("====================")

print(count)