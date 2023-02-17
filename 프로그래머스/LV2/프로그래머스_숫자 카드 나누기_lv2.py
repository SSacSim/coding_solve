arrayA = [10, 17]
arrayB = [5, 20]

arrayA_min = min(arrayA)

A_answer = 0 

min_list = []
for i in range(1, int(arrayA_min**(1/2)) + 1 ):
  if arrayA_min % i == 0:
    min_list.append(i)
    min_list.append(arrayA_min // i)

min_list.sort(reverse = True)
for i in min_list:
  A_flag = 0
  for j in arrayA:
    if j % i != 0 :
      A_flag = 1
      break
  if A_flag == 0:
    A_answer =i
    break

for i in arrayB:
  if A_answer == 0 or i % A_answer == 0:
    A_answer = 0
    break
    
arrayB_min = min(arrayB)

B_answer = 0 

min_list = []
for i in range(1, int(arrayB_min**(1/2)) + 1 ):
  if arrayB_min % i == 0:
    min_list.append(i)
    min_list.append(arrayB_min // i)

min_list.sort(reverse = True)
for i in min_list:
  B_flag = 0
  for j in arrayB:
    if j % i != 0 :
      B_flag = 1
      break
  if B_flag == 0:
    B_answer =i
    break
for i in arrayA:
  if B_answer == 0 or i % B_answer == 0:
    B_answer = 0
    break
    
print(max(A_answer,B_answer)
