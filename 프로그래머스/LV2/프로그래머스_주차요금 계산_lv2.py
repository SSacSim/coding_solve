fees = [1, 461, 1, 10] # 기본 시간(분) /	기본 요금(원)	/단위 시간(분)	/단위 요금(원)
records = ["00:00 1234 IN"]

my_dict = dict()

new_records = []
for i in records:
  temp = i.split(" ")
  time = temp[0].split(":")
  sum_time = int(time[0]) * 60 + int(time[1])
  new_records.append([temp[1],sum_time,temp[2]])

new_records.sort(key = lambda x : (int(x[0]),x[1]))

for i in new_records:
  if i[0] not in my_dict:
    my_dict[i[0]] = [i[1]]
  else:
    my_dict[i[0]].append(i[1])

# 입출 맞지 않는것 처리
last_time = 23*60 + 59
for i in my_dict:
  if len(my_dict[i]) % 2 != 0:
    my_dict[i].append(last_time)

import numpy as np
answer = []
for i in my_dict:
  temp = my_dict[i]
  
  result = 0
  use_time = 0
  for i in range(0, len(temp), 2):
    use_time += temp[i+1] - temp[i]
  
  if use_time <= fees[0]:
    result = fees[1]
  else:
    result = fees[1] + np.ceil((use_time - fees[0]) / fees[2]) * fees[3]
  
  answer.append(int(result))

print(answer)