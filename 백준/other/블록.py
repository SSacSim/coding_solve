loop = int(input())

for i in range(loop):
  temp = list(map(int,input().split(" ")))
  answer= "No"
  if sum(temp) == 0:
    print(answer)
  else:
    temp[1] %= 2
    
    if temp[1] == 0 : # 1x1과 ㄴ으로만 블록을 만들어야함
      if temp[2] <= temp[0] and ((temp[0] -temp[2]) %2 == 0):
        answer = "Yes"
    else: # 2x1 블럭이 하나 남았으므로 1. 1x1 , ㄴ블록 사용한 후 나머지
      if temp[2] <= temp[0] and ((temp[0] -temp[2]) %2 == 0) and temp[0] != 0:
        answer = "Yes"
    print(answer)
