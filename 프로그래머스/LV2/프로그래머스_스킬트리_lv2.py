skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
skill = list(skill)

store = []
for i in skill_trees:
  temp = []
  for j in i:
    if j in skill:
      temp.append(j)
  store.append(temp)

count = 0
for i in store:
  flag= 0
  for index, j in enumerate(i):
    if skill[index] != j:
      flag = 1
      break
    
  if flag == 0:
    count +=1

print(count)