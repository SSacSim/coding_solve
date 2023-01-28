k = 2
tangerine = [1, 1, 1, 1, 2, 2, 2, 3]

from collections import Counter

temp_dict = dict(Counter(tangerine))
store = []
for i , j in temp_dict.items():
  store.append([i,j])

store.sort(key= lambda x : -x[1])
count = 0
answer = 0
for index,(i, j) in enumerate(store):
  count += j
  if count >=k:
    answer = index + 1
    break

print(answer)