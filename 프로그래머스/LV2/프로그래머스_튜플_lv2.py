s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
s = s[1:-1]

change = []
temp_list = []
before = ""
for i in s:
  
  if ord(i) == 123: #{
    temp =""
  elif ord(i) == 125: # }
    change.append(list(map(int,list(temp.split(",")))))
  else:
    temp +=i

change.sort(key = lambda x: len(x))

answer = []
my_dict = dict()
for i in change:
  for j in i:
    if j not in my_dict:
      my_dict[j] = 1
      answer.append(j)
      break

print(answer)