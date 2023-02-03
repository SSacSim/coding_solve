expression = "50*6-3*2"
expression += " "
express_list = []
temp = ""
for i in expression:
  if ord(i) >= 48 and ord(i) <= 57:
    temp += i
  else:
    express_list.append(int(temp))
    express_list.append(i)
    temp = ""
  
six_list = [["*","-","+"] ,["*","+","-"],
            ["+","-","*"] ,["+","*","-"],
            ["-","*","+"] ,["-","+","*"]]

from collections import deque

max_value = 0
left_que_raw = deque(express_list[:-1])
right_que_raw = deque(express_list[:-1])
for i in six_list: # 6가지 가지슈
  print("i",i)
  right_que = right_que_raw.copy()
  left_que = left_que_raw.copy()
  for j in i : # 우선순위 수식
    right_que = left_que.copy()
    left_que = deque([])
    print("j",j)
    while True:
      if len(right_que) == 0:
        break
      k = right_que.popleft()
      print("k",k)
      if k == j and k == "*":
        left_que.append(left_que.pop() * right_que.popleft())
      elif k ==j and k ==  "+":
        left_que.append(left_que.pop() + right_que.popleft())
      elif k == j and k == "-":
        left_que.append(left_que.pop() - right_que.popleft())
      else:
        left_que.append(k)
      print("left_que2", left_que)
      print("right_que2", right_que)

    print("left_que", left_que)
    print("right_que", right_que)

  if len(left_que) == 1:
    temp = abs(left_que.popleft())
    if temp > max_value:
      max_value = temp
  
  print("max_value",max_value)
  print("==========================")
print(max_value)
