from itertools import combinations

orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course =[2,3,4]

my_map = dict()

for i in orders:
  i = "".join(sorted(i))
  for n in range(2,len(i)+1):
    for j in combinations(list(i) , n):
      print(j)
      temp = "".join(j)
      temp_r = temp[::-1]
      
      if temp not in my_map:
        if temp_r not in my_map:
          my_map[temp] = 1
        else:
          my_map[temp_r] +=1
      else:
        my_map[temp] += 1

result = list(my_map.items())
result.sort(key = lambda x : ( len(x[0]) , -x[1] ) )
answer = []
for i in course:
  temp_max = 0
  for j in result:
    print("j",j)
    if len(j[0]) == i:
      if j[1] <= 1:
        break
      if temp_max <= j[1]:
        temp_max = j[1]
        answer.append(j[0])
      else:
        break
  print("=====================")

answer.sort(key = lambda x :x)
print(answer)