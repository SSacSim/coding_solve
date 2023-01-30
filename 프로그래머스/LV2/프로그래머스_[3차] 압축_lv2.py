from collections import deque
msg = 'KAKAO'

my_que = deque(list(msg))

my_dict = dict()

for index, i in enumerate(range(ord("A") , ord("Z")+1)):
  my_dict[chr(i)] = index + 1

now_index = 27

answer = []
while True:
  print("my_que",my_que)
  if len(my_que) == 0:
    break

  store_temp = ""
  while True:
    pop_char = my_que.popleft()
    print('pop_char',pop_char)
    if (store_temp + pop_char) in my_dict:
      store_temp += pop_char
      if len(my_que) == 0:
        answer.append(my_dict[store_temp])
        break
    else:
      print("else 실행")
      my_dict[store_temp + pop_char] = now_index
      now_index += 1
      answer.append(my_dict[store_temp])
      print("저장",my_dict[store_temp])
      print("저장char",store_temp)
      my_que.appendleft(pop_char)
      break
  print("==============================")

print(answer)