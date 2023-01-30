files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]

#head, number ,tail을 구하자
new_set = []
for i_index ,i in enumerate(files):
  head = ""
  number = ""
  tail = ""
  flag = 0
  str_number = ""
  for j_index, j in enumerate(i):
    if ord(j) >=48 and ord(j) <= 57: #숫자를 만나면 
      str_number +=j
      if flag == 0:
        flag = 1
        head = i[:j_index]
    else:
      if flag == 1:
        tail = i[j_index:]
        number = str_number
        break
  number = str_number
  print(number)
  print(head.lower())
  new_set.append([head.lower(),int(number),tail, i_index])

new_set.sort(key = lambda x : (x[0],x[1]))
answer = []
for i in new_set:
  answer.append(files[i[3]])

print(answer)