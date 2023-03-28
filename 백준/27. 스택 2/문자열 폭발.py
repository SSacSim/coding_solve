import sys
from collections import deque
input = sys.stdin.readline
string_list = input().strip()
target = list(input().strip())

temp_stack1 = deque([]) # 최종 정답이 기록되는 곳
temp_stack2 = deque([]) # 부분 집합이 기록되는 곳 
target_deque = deque(target)
for i in string_list:
  if len(temp_stack2) < len(target) - 1 : #다 넣는다
    temp_stack2.append(i)
    continue
  
  else:
    temp_stack2.append(i)
  # temp_stack2가 target과 길이가 같으면 같은 문자인지 확인
    while True:
      if temp_stack2 != target_deque:
        if len(temp_stack2) == len(target_deque):
          temp_stack1.append(temp_stack2.popleft())
        break
      if temp_stack2 == target_deque: # 같은 문자일때
        temp_stack2 = deque([])
        while len(temp_stack1) != 0 and len(temp_stack2) < len(target):
          temp_stack2.appendleft(temp_stack1.pop())
    

while True:
  if len(temp_stack2) == 0:
    break
  temp_stack1.append(temp_stack2.popleft())
if len(temp_stack1) == 0:
  print("FRULA")
else:
  print("".join(temp_stack1))
