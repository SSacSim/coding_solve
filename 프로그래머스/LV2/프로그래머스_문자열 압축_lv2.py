s = "abcabcdede"

min_count = len(s)
for i in range(1,len(s)//2+ 1): # 몇개씩 묶냐?
  my_dict = []
  count = 0
  before_str = None
  j = 0
  while True:
    if j >= len(s) + 1 :
      my_dict.append(s[j - i: len(s) + 1])
      count += len(str(s[j - i: len(s) + 1]))
      break

    if before_str == None:
      print("None" , j)
      before_str = s[j:j+i]
      before_num = 1
    else:
      if before_str == s[j:j+i]:
        print("before == s " , j)
        before_num  += 1
      else:
        if before_num == 1:
          my_dict.append(str(before_str))
          count += len(str(before_str))
        else:
          my_dict.append(str(before_num)+str(before_str))
          count += len(str(before_num)+str(before_str))
        before_str = s[j:j+i]
        before_num = 1
    j += i
  print(my_dict)
  print(count)
  if count < min_count:
    min_count = count
  print("====================")

print(min_count)
