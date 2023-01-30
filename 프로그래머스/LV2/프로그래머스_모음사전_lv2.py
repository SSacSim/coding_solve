from itertools import permutations, combinations , product
word = "AAAE"

word_store = ["A","E","I","O","U"]

map_dict = []
for j in range(1,6):
  for i in product(word_store,repeat = j):
    temp = "".join(i)
    map_dict.append(temp)

map_dict.sort()

for i_index, i in enumerate(map_dict):
  if i == word:
    answer = i_index
    break

print(answer + 1)