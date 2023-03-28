import sys
input = sys.stdin.readline
T = int(input().strip())

for _ in range(T):
  target = int(input().strip())
  while True:
    flag = 0
    new  = int(target **(1/2))
    for i in range(new , 1, -1):
      if target % i == 0:
        flag = 1
        break
    
    if flag == 1:
      target += 1
    else:
      if target <= 1:
        print(2)
      else:
        print(target)
      break
# 입력 범위가 0부터 시작이라는 점을 주의
