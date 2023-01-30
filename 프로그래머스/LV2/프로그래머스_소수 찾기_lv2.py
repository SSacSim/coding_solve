numbers = "011"
from itertools import permutations
max_value = int("".join(sorted(list(numbers),reverse = True)))
sosu = [0 for _ in range(max_value +1)]

for i in range(2,max_value +1):
  temp = 2
  if sosu[i] == 1:
    continue
  while True:
    if (i * temp) > max_value:
      break
    
    sosu[i * temp] = 1 # 소수가 아님
    temp += 1

sosu[0] , sosu[1]  = 1, 1 
count = 0
answer = []
for j in range(1, len(numbers) +1 ):
  for i in permutations(list(numbers), j):
    temp = int("".join(i))
    if temp not in answer and sosu[temp] == 0:
      count += 1 
      answer.append(temp)
print(count)