from collections import Counter

want = ["banana", "apple", "rice", "pork", "pot"]
number = [2, 2, 2, 2, 1]
discount = ["chicken", "apple", "apple", "banana"]

dicsount_dict = dict(Counter(discount[:9]))
want_dict = dict()

for i,j in zip(want,number):
  want_dict[i] = j

count = 0
for index,i in enumerate(discount[9:]):
  print('dicsount_dict',dicsount_dict)
  print("input",i)
  print(index)
  
  if i not in dicsount_dict:
    dicsount_dict[i] = 1
  else:
    dicsount_dict[i] += 1

  # 가능한지 체크
  for j in want_dict.keys():
    flag = 0
    print("want_dict",j)
    if j not in dicsount_dict:
      print("없음1")
      flag = 1
      break
    else:
      if dicsount_dict[j] < want_dict[j]:
        print("없음2")
        flag = 1
        break
  if flag == 0:
    count += 1
  
  
  dicsount_dict[discount[index]] -=1
  print("==============================")

print(count)