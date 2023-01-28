s = "abbb"
list_s = list(s)

#odd search
max_len = 0
for i in range(1 , len(list_s)) : # 1부터 시작 # odd 
  count = 1
  j = 1
  print("기준점",i)
  while True:
    if i - j <0 or i + j >= len(list_s):
      break
    print("i-j",list_s[i-j])
    print("i+j",list_s[i+j])
    if list_s[i - j] != list_s[i + j]:
      print("count",count)
      break
    else:
      count += 2
      if max_len < count:
        max_len = count

    j += 1
  print("====================")

# even
max_len2 = 0
for i in range(0 , len(list_s) - 1) : # 1부터 시작 # even 
  count = 0
  j = 0
  print("기준점",i)
  while True:
    if i - j <0 or i + j + 1 >= len(list_s):
      break
    print("i-j",list_s[i-j])
    print("i+j",list_s[i+j+1])
    if list_s[i - j] != list_s[i + j+1]:
      print("count",count)
      break
    else:
      count += 2
      if max_len2 < count:
        max_len2 = count

    j += 1
  print("====================")

answer = max_len if max_len > max_len2 else max_len2

