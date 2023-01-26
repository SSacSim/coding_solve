gems =["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
list_gems= list(set(gems))
my_dict = dict()
start_index = 0
end_index = 0
answer_start = 0
answer_end = 0
answer = 99999999
for index, i in enumerate(gems):
  print('my_dict' , my_dict)
  print("start",start_index)
  print("end",end_index)

  if i not in my_dict:
    my_dict[i] = 1
  else:
    my_dict[i] +=1
  end_index = index
  print("after",my_dict)
  while True:
    if start_index > end_index:
      break
    if len(my_dict) == len(list_gems):
      if answer > (end_index - start_index):
        answer_start = start_index
        answer_end = end_index
        answer = (end_index - start_index)
  
      my_dict[gems[start_index]] -=1
      if my_dict[gems[start_index]] == 0:
        del my_dict[gems[start_index]]
      start_index +=1
    else:
      break
  print("===================")
print(answer_start+1,answer_end+1)