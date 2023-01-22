progresses =   [20, 99, 93, 30, 55, 10]
speeds =       [5, 10, 1, 1, 30, 5]

import numpy as np
temp = []
for pro, speed in zip(progresses, speeds):
  temp.append(np.ceil((100 - pro) / speed))
print(temp)

temp.append(999999999999)

now_day = temp[0]

count = 1
answer= []
for i in temp[1:]:
  print(i)
  print(now_day)
  if now_day >= i:
    count +=1 
  else:
    answer.append(count)
    now_day = i
    count = 1

  print("answer",answer)
  print("--------------------")
print(answer)