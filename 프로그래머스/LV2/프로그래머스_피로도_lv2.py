from itertools import permutations
k = 80
dungeons = [[80,20],[50,40],[30,10]]
d_list = list(permutations(dungeons, len(dungeons)))
answer = 0
for i in d_list:
  now_k = k
  count = 0
  for j in i:
    print(j)
    if now_k >=j[0]:
      now_k -= j[1]
      count +=1
    
    if answer < count:
      answer = count
  print("==============")